# Order To Cash Business Report



## Overview

    Report simulates real-world downstream order to cash business report.  
    Alkaline Battery Technologies and Buy n Large are fictitious companies, brands, and logos.

    Report has three primary uses:
        1. Provide visuals to inform business leaders' data-driven decisions
        2. Real-time data allows for the business to solve issues as they appear real-time
        3. Provide drill-down reports for customer service, sales, and logistics groups to see individual line data from multiple sources in one location
            Without this visual, they could only see data from different source systems separately.  Joining the supply chain and order management data with                     product data, customer data allows efficient problem-solving and insights.

    Metrics chosen from https://www.datapine.com/blog/supply-chain-metrics-and-kpis/

    Data generated in python script GenerateData.py.  
    All data is fictional and does not represent any organization's real financial data. 
    Real, raw financial, customer, and product data is hard to come by as no organization wants to reveal or generate that data for the public.

### Assumptions:
    All data comes from a data lake or other data repository.

    Data has a pipeline from source to repository allows for near real-time data.
        
    Depending on business processes and architecture, data processing and cleaning could occur in a third-party analytics system or Power Query.
    For the purpose of this dashboard, assuming all data processing and cleaning is performed in a third-party analytics system.
    Performing the least amount of Power Query applied steps as necessary.

    All data is for a rolling 12-month period: current month and previous 11 months.

    Customer data (name and id), product data (name and id), and shipping locations (name and id) are all located in separate locations, whether it be SharePoint files, data lakes, or other table locations. 
    All can be joined with data on id. 

    Order to Cash Cycle Time Metric:
    Measures the days between the purchase to reporting after payment is collected. 
    For the purpose of this dashboard, we are measuring the days between the ordered date and the invoice date.

    Goals are kept in a separate SharePoint file. If the business wants to change its goals, it will not break the dashboard.

### Power Query

    Rolling 12-month period
        Date field from the source table that the month will be based off of
            Invoice - invoice date
            Automated - ordered date
            Supply Chain - ordered date
            Order Management - ordered date
        If the business wants to change the field, which determines the month, it can be changed in Power Query.

        For each source table the following column is added
        = Table.AddColumn(#"Changed Type", "Month Order", each if (Date.Month([Ordered Date]) ) = Date.Month(DateTime.LocalNow()) then 12 else Number.Mod( (Date.Month([Ordered Date]) - Date.Month(DateTime.LocalNow())+12),12), type number)

    Order to Cash Cycle Time
        For the invoice table, a column is created for the order to cash cycle time calculation.
        Invoice Date - Ordered Date

    Parameter for Environment
        Parameter to easily change source environment to development, staging, and production.

### Data View

    Date to be listed as Earliest Month (current month - 11) to Current Month
        'Month' table - 'Date' field is sorted by 'Month Order'

    Product to be listed in order 'Power, Chargers, Lighting, Other'
        'Product' table - 'Product' field is sorted by 'Product Order'

### Model

    Invoice, Automation, Supply Chain, Order Management tables have a many to 1 relationship with the month, product, and shipping location tables.

![image](https://github.com/pngu-pngu/Order-To-Cash-Business-Report/assets/118928534/fb744046-8ddf-4d77-a7a8-ea5e09b58f4b)


### Pages
    Home Page 
    Executive Dashboard 
    Performance Summary 
    Performance Summary Details 
    Supply Chain Details 
    Order Management Details 
    Invoice Details 
    Automation Details 

  #### Home Page

    Background image used is royalty free stock image.
    
    The report provides an overview of six downstream order to cash key performance indicators for Alkaline Battery Technologies.
    Alkaline Battery Technologies is a division of the Buy n Large brand providing industrial power, lighting, and chargers to the world's leading industries.

    Last Refresh - The date and time the report was last refreshed. Note this is not when the data was last refreshed.
        Refresh time is from a world time api.  It is EST.
        
    Page Navigator - Click any page button on the left side of the report, and the user will be taken to that page.
![HomePage](https://github.com/pngu-pngu/Order-To-Cash-Business-Report/assets/118928534/b1ee6411-858f-4d00-b18e-575b04e98b62)


  #### Executive Dashboard 

      Detailed definitions of KPIs and drill-down reports.
![ExecutiveDashboard](https://github.com/pngu-pngu/Order-To-Cash-Business-Report/assets/118928534/e6387ed7-c997-46ba-9dc4-55816e9a55d5)

  #### Performance Summary 
      Six KPIs are displayed as visuals on a line chart.  The red dotted line is the current business goal.
![PerformanceSummary](https://github.com/pngu-pngu/Order-To-Cash-Business-Report/assets/118928534/0eb7c138-76a4-4e65-8971-90965e26e0e5)

  #### Performance Summary Details 
      Detailed matrix of six KPI values, as well as calculated value quantities.
![PeformanceSummaryDetails](https://github.com/pngu-pngu/Order-To-Cash-Business-Report/assets/118928534/5f94785e-5383-4c35-9514-9689888846a3)

  #### Supply Chain Details 
![SupplyChainDetails](https://github.com/pngu-pngu/Order-To-Cash-Business-Report/assets/118928534/61e8db1a-3475-48a5-87ff-bab34108245d)

  #### Order Management Details 
![OrderManagementDetails](https://github.com/pngu-pngu/Order-To-Cash-Business-Report/assets/118928534/e22a7248-eb5a-4c1b-9962-8dc78a7f0fd1)

  #### Invoice Details 
![InvoiceDetails](https://github.com/pngu-pngu/Order-To-Cash-Business-Report/assets/118928534/190eccd4-c5d0-4bf6-9292-600027822fc8)

  #### Automation Details 
![image](https://github.com/pngu-pngu/Order-To-Cash-Business-Report/assets/118928534/f2216014-2771-404e-bc84-6473fb31e17f)


### Filters
    Filters on each page.
![image](https://github.com/pngu-pngu/Order-To-Cash-Business-Report/assets/118928534/cadaceae-1a2c-41bc-b49e-dbeb76452192)
    Clicking on the visual will reveal additional filters.
![image](https://github.com/pngu-pngu/Order-To-Cash-Business-Report/assets/118928534/c065d876-4c49-4a31-a642-f2d6a78f9051)

## In Progress
    Use Power Automate to send email to business leaders with a summary of KPI performance at the end of every month.
    Create pipeline from a repository through a big data processing tool to perform predictive analytical functions that feed into the report.

