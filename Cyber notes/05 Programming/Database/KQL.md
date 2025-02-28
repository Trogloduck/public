*Kusto Query Language: explore data to discover patterns, identify anomalies and outliers, and create statistical models; input/output: tabular*

- [[#Basics]]
- [[#Operators]]
	- [[#Select]]: [[#` take`]], [[#` project`]], [[#` project-away`]]
	- [[#Filter]]: [[#` where`]], [[#`has`]], [[#`contains`]], [[#`datetime`]]
	- [[#Sort]]: [[#` sort by`]], [[#` top`]]

___
### Basics

Query
- Read-only
- Operators sequenced by "**`|`**"
- Data flows from one operator to the next in a **sequential** fashion
- Can be one line (several lines for clarity)

*Example:*
```KQL
StormEvents 
| where StartTime between (datetime(2007-11-01) .. datetime(2007-12-01))
| where State == "FLORIDA"  
| count
```
1. Search in StormEvents table
2. Filter by StartTime and State columns (`| where`)
3. Return # results (`| count`)

##### Common line - Database selection
Always start query with name of database to search in
```KQL
StormEvents
```

### Operators
#### Select
##### `| take`
**Limit** # results
```KQL
StormEvents
| take 5
```
*return 5 1st rows*

##### `| project`
**Select** particular **columns** to return
```KQL
| project EventType, State, DamageProperty, DamageCrops, InjuriesDirect, InjuriesIndirect
```
Can be used to compute columns together into new columns:
```KQL
| project Damage = DamageProperty + DamageCrops
```

##### `| project-away`
**Exclude** particular columns
```KQL
| project-away EpisodeId, EventId
```

#### Filter
##### `| where`

```KQL
| where DamageProperty > 0
```

```KQL
| where StartTime > ago(365d)
```
*return results later than 1 year ago*

```KQL
| where State == "FLORIDA"
```

###### `has`
```KQL
| where EventType has "wind"
```
*return results **matching** the **word** "wind"*

###### `contains`
```KQL
| where EventType contains "free"
```
*return results **including substring** "free"*

###### `datetime`
```KQL
| where` _time_ `between` `(datetime(`_value_`)..datetime(`_value_`))
```

```KQL
| where StartTime between (datetime(2007-01-01)..datetime(2007-06-01))
```

#### Sort

##### `| sort by`

Sort by \[Property] desc (default) or asc
```KQL
| sort by DamageProperty
```

Sort on **several properties** (then order is really important), can be used to group by \[property]
```
| sort by State asc, DamageProperty
```
*Sort by State alphabetically, then sort by DamageProperty desc*

##### `| top`
```KQL
| top 10 by DamageProperty
```


Challenge:
- April 2007: `| where StartTime between (datetime(2007-04-01)..datetime(2007-05-01))`
- Top 5 damage (property + crops):
```KQL
| project Damage = DamageProperty + DamageCrops
| top 5 by Damage
```
- Virginia: `| where State == "VIRGINIA"`

Full query:
```KQL
StormEvents
| where State == "VIRGINIA"
| where StartTime between (datetime(2007-04-01)..datetime(2007-05-01))
| project EventId, Damage = DamageProperty + DamageCrops
| top 5 by DamageProperty
```



___
Course: https://learn.microsoft.com/en-us/training/modules/write-first-query-kusto-query-language
Practice on https://dataexplorer.azure.com/clusters/help


References:
https://learn.microsoft.com/en-us/kusto/query/queries
https://learn.microsoft.com/en-us/kusto/query/kql-quick-reference