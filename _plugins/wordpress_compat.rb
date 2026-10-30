# Keeps the URL surface of the old WordPress site working on the static build.
#
#   /category/<slug>/, /tag/<slug>/   term archives, using the WordPress slug from _data/terms.json
#                                     (new terms fall back to Jekyll's slugify, which matches WordPress for ASCII)
#   /YYYY/, /YYYY/MM/, /YYYY/MM/DD/   date archives
#   /wp-ids.json                      WordPress post/page ID -> URL, used to redirect old /?p=123 links
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
          slug = WordPressCompat.term_slug(site, key, name)
          add(site, "#{prefix}/#{CGI.unescape(slug)}", "#{prefix.capitalize}: #{name}", posts)
        end
      end

      { "%Y/%m/%d" => "%B %-d, %Y", "%Y/%m" => "%B %Y", "%Y" => "%Y" }.each do |dir_format, title_format|
        site.posts.docs.group_by { |p| p.date.strftime(dir_format) }.each do |dir, posts|
          add(site, dir, posts.first.date.strftime(title_format), posts)
        end
      end

      site.data.fetch("redirects", {}).each do |from, to|
        stub = Jekyll::PageWithoutAFile.new(site, site.source, CGI.unescape(from).delete_prefix("/"), "index.html")
        stub.data = { "layout" => "redirect", "redirect_to" => to, "sitemap" => false }
        site.pages << stub
      end

      ids = (site.posts.docs + site.pages).each_with_object({}) { |d, h| h[d.data["wp_id"].to_s] = d.url if d.data["wp_id"] }
      ids_page = Jekyll::PageWithoutAFile.new(site, site.source, "", "wp-ids.json")
      ids_page.content = JSON.generate(ids)
      ids_page.data = { "layout" => nil, "sitemap" => false }
      site.pages << ids_page
    end

    private

    def add(site, dir, title, posts)
      site.pages << ArchivePage.new(site, dir, "title" => title, "archive_posts" => posts.sort_by(&:date).reverse)
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
