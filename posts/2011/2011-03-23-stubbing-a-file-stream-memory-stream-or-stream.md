---
title: Stubbing a File Stream, Memory Stream, or Stream
date: 2011-03-23 10:23:04 -0700
last_modified_at: 2011-03-23 15:37:30 -0700
permalink: /2011/03/23/stubbing-a-file-stream-memory-stream-or-stream/
slug: stubbing-a-file-stream-memory-stream-or-stream
wp_id: 2464
original_url: https://compositecode.blog/2011/03/23/stubbing-a-file-stream-memory-stream-or-stream/
categories:
- .NET Bits
- How-to
tags:
- filestream
- memorystream
- mock
- stream
- stub
excerpt: Here’s the class that has a Func setup as a property. The reason this is setup, is so that the stream can actually be stubbed on the ComplianceReportingJob. Otherwise if the Stream was just being used as is, instantiated in the class, or passed in via injection, we still couldn’t get it mocked or stubbed. Especially if the class ComplianceReportingJob is under test.
---

Here’s the class that has a Func setup as a property. The reason this is setup, is so that the stream can actually be stubbed on the ComplianceReportingJob. Otherwise if the Stream was just being used as is, instantiated in the class, or passed in via injection, we still couldn’t get it mocked or stubbed. Especially if the class ComplianceReportingJob is under test.

```csharp
public class ComplianceReportingJob : IJob
{
    readonly ITradeRepository tradeRepo;
    readonly IFileSystem fileSys;

    public ComplianceReportingJob(ITradeRepository tradeRepository, IFileSystem fileSystem)
    {
        tradeRepo = tradeRepository;
        StreamedFile = filename => new FileStream(filename, FileMode.Create);
    }

    public Func<string, Stream> StreamedFile { get; set; }
}
```

What we have here is the context being setup, with the property being stubbed with a fake StreamedFile = filename => new MemoryStream(). So if you’re looking for a way to test streams with .NET, this is a way around the limitations of the framework.

```csharp
public class with_a_compliance_report_job
{
    protected static ITradeRepository tradeRepository;
    protected static IFileSystem fileSys;
    protected static ComplianceReportingJob job;

    Establish context = () =>
    {
        tradeRepository = Substitute.For<ITradeRepository>();
        fileSys = Substitute.For<IFileSystem>();

        reportContent = FizzWare.NBuilder.Builder<TradeComplianceViewModel>.CreateListOfSize(10).Build().ToList();

        tradeRepository.GetComplianceReport().Returns(reportContent);
        fileSys.DirectoryExists(string.Empty).ReturnsForAnyArgs(true);

        job = new ComplianceReportingJob(tradeRepository, fileSys)
                    {StreamedFile = filename => new MemoryStream()};
    };

    protected static List<TradeComplianceViewModel> reportContent;
}
```

This is a pretty sweet solution, for now. The ideal solution however, would be that Microsoft fixes the framework, which is very unlikely to happen. The whole closed, sealed, and otherwise locked up framework stack is a massive problem with testability. Which then directly impacts maintainability and other things over time.

[![Shout it](http://dotnetshoutout.com/image.axd?url=http%3A%2F%2Fcompositecode.com%2F2011%2F03%2F23%2Fstubbing-a-file-stream-memory-stream-or-stream%2F)](http://dotnetshoutout.com/Stubbing-a-File-Stream-Memory-Stream-or-Stream-Composite-Code)
