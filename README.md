# Order To Cash Business Report

## Overview

    Report simulates real-world downstream order to cash business report.  
    Alkaline Battery Technologies and Buy n Large are fictitious companies, brands, and logos.

    Data generated in python script GenerateData.py.  
    All data is fictional and does not represent any organization's real financial data. 
    Real, raw financial data is hard to come by as no organization wants to reveal or generate that data for the public.

#### Assumptions:
    All data comes from a data lake or other data repository.
        
    Depending on business processes and architecture, data processing and cleaning could occur in a third-party analytics system or Power Query.
    For the purpose of this dashboard, assuming all data processing and cleaning is performed in a third-party analytics system.
    Performing the least amount of Power Query applied steps as necessary.

    All data is for a rolling 12-month period: current month and previous 11 months.

    Customer data (name and id), product data (name and id), and shipping locations (name and id) are all located in separate locations, whether it be SharePoint files, data lakes, or other table locations. 
    All can be joined with data on id. 

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

    Page Navigator - Click any page button on the left side of the report, and the user will be taken to that page.
  #### Executive Dashboard 
  #### Performance Summary 
  #### Performance Summary Details 
  #### Supply Chain Details 
  #### Order Management Details 
  #### Invoice Details 
  #### Automation Details 
