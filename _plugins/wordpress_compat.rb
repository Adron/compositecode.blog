# Keeps the URL surface of the old WordPress site working on the static build.
#
#   /category/<slug>/, /tag/<slug>/   term archives, using the WordPress slug from _data/terms.json
#                                     (new terms fall back to Jekyll's slugify, which matches WordPress for ASCII)
#   /YYYY/, /YYYY/MM/, /YYYY/MM/DD/   date archives
#   /author/adron/                    author archive
#                                     every archive paginates like WordPress: <archive>/page/N/, `paginate` posts each
#   /wp-ids.json                      WordPress post/page ID -> URL, used to redirect old /?p=123 links
#   /archives/months.json             [url, "Month YYYY"] pairs for the sidebar archive dropdown (filled in by JS,
#                                     so ~12 KB of <option>s isn't repeated on every page)
#   _data/redirects.yml               old path -> current path, emitted as meta-refresh redirect pages
#
# It also prefixes root-relative links with site.baseurl when one is set, so the github.io preview
# (served under /compositecode.blog/) works even though post bodies link to /2026/... and /wp-content/....
require "cgi"
require "json"

module WordPressCompat
  TERM_PREFIX = { "categories" => "category", "tags" => "tag" }.freeze

  def self.term_slug(site, key, name)
    site.data.dig("terms", key, name) || Jekyll::Utils.slugify(name)
  end

  class ArchivePage < Jekyll::PageWithoutAFile
    def initialize(site, dir, data)
      super(site, site.source, dir, "index.html")
      self.data = { "layout" => "archive" }.merge(data)
    end
  end

  class Generator < Jekyll::Generator
    safe true
    priority :low

    def generate(site)
      TERM_PREFIX.each do |key, prefix|
        site.public_send(key).each do |name, posts|
          add(site, "#{prefix}/#{WordPressCompat.term_slug(site, key, name)}", prefix.capitalize, name, posts)
        end
      end

      { "%Y/%m/%d" => ["Day", "%B %-d, %Y"], "%Y/%m" => ["Month", "%B %Y"], "%Y" => ["Year", "%Y"] }.each do |dir_format, (label, name_format)|
        site.posts.docs.group_by { |p| p.date.strftime(dir_format) }.each do |dir, posts|
          add(site, dir, label, posts.first.date.strftime(name_format), posts)
        end
      end

      author = site.config.fetch("author", {})
      add(site, author["url"].to_s.delete_prefix("/").chomp("/"), "Author", author["display_name"], site.posts.docs) if author["url"]

      site.data.fetch("redirects", {}).each do |from, to|
        stub = Jekyll::PageWithoutAFile.new(site, site.source, CGI.unescape(from).delete_prefix("/"), "index.html")
        stub.data = { "layout" => "redirect", "redirect_to" => to, "sitemap" => false }
        site.pages << stub
      end

      months = site.posts.docs.group_by { |p| p.date.strftime("%Y/%m") }
                    .map { |dir, posts| ["/#{dir}/", posts.first.date.strftime("%B %Y")] }.reverse
      add_json(site, "archives", "months.json", months)

      ids = (site.posts.docs + site.pages).each_with_object({}) { |d, h| h[d.data["wp_id"].to_s] = d.url if d.data["wp_id"] }
      add_json(site, "", "wp-ids.json", ids)
    end

    private

    def add_json(site, dir, name, value)
      page = Jekyll::PageWithoutAFile.new(site, site.source, dir, name)
      page.content = JSON.generate(value)
      page.data = { "layout" => nil, "sitemap" => false }
      site.pages << page
    end

    # dir is the archive's URL path without slashes (may be percent-encoded, as WordPress slugs can be).
    def add(site, dir, label, name, posts)
      chunks = posts.sort_by(&:date).reverse.each_slice(site.config.fetch("paginate", 5)).to_a
      path = ->(n) { n == 1 ? "/#{dir}/" : "/#{dir}/page/#{n}/" }
      chunks.each.with_index(1) do |chunk, n|
        site.pages << ArchivePage.new(site, CGI.unescape(path.call(n)),
          "title" => "#{label}: #{name}", "archive_label" => label, "archive_name" => name,
          "archive_posts" => chunk, "sitemap" => n == 1,
          "next_page_path" => (path.call(n + 1) if n < chunks.size),  # older posts
          "previous_page_path" => (path.call(n - 1) if n > 1))       # newer posts
      end
    end
  end

  module Filters
    # {{ name | term_url: "categories" }} -> /category/<wordpress-slug>/
    def term_url(name, key)
      "/#{TERM_PREFIX.fetch(key)}/#{WordPressCompat.term_slug(@context.registers[:site], key, name)}/"
    end
  end

  ROOT_RELATIVE = /(\s(?:href|src|action|poster)=["'])\/(?!\/)/

  Jekyll::Hooks.register [:pages, :documents], :post_render do |doc|
    base = doc.site.config["baseurl"].to_s.chomp("/")
    next if base.empty? || doc.output_ext != ".html"

    doc.output = doc.output.gsub(ROOT_RELATIVE) { "#{Regexp.last_match(1)}#{base}/" }
  end
end

Liquid::Template.register_filter(WordPressCompat::Filters)
