# Web Site Performance Metrics Reporter

## Intro
The goal of this project is to show my SQL (PostgreSQL) and Python skills applied to generate performance reports for a fictional Web News website.

### Features
- Clean and modular code - ready to provide more reports

## Reports
Run one of the following methods from App.py from python interactive:
### All reports
`reportAll()`: Prints all three of the below metrics
`method`: what are the most popular three

### What are the most popular three articles of all time?
Which articles have been accessed the most? Information is presented as a sorted list with the most popular articles at the top.

#### Example:
    Princess Shellfish Marries Prince Handsome — 1201 views
    Baltimore Ravens Defeat Rhode Island Shoggoths — 915 views
    Political Scandal Ends In Political Scandal" — 553 views


### Who are the most popular article authors of all time? 
That is, which authors has the most page views? Presented  as a sorted list with the most viewed author at the top.

#### Example:
    Ursula La Multa — 2304 views
    Rudolf von Treppenwitz — 1985 views
    Markoff Chaney — 1723 views
    Anonymous Contributor — 1023 views

### On which days did more than 1% of web requests lead to errors? 
The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

#### Example:

    July 28, 2016 — 3.0% errors
    July 29, 2016 — 2.5% errors
    July 30, 2016 — 1.5% errors

## Files
- App.py: Provides methods to view each report as well as all reports at once
- newsdata.sql: Fictonal database which is used to generate these reports


## Database
- SQL: PostgreSQL(v9.5.10)
- Database name: news

### Table: Articles
<table border="1">
  <tr>
    <th align="center">Column</th>
    <th align="center">Type</th>
    <th align="center">Modifiers</th>
  </tr>
  <tr valign="top">
    <td align="left">author</td>
    <td align="left">integer</td>
    <td align="left">not null</td>
  </tr>
  <tr valign="top">
    <td align="left">title</td>
    <td align="left">text</td>
    <td align="left">not null</td>
  </tr>
  <tr valign="top">
    <td align="left">slug</td>
    <td align="left">text</td>
    <td align="left">not null</td>
  </tr>
  <tr valign="top">
    <td align="left">lead</td>
    <td align="left">text</td>
    <td align="left">&nbsp; </td>
  </tr>
  <tr valign="top">
    <td align="left">body</td>
    <td align="left">text</td>
    <td align="left">&nbsp; </td>
  </tr>
  <tr valign="top">
    <td align="left">time</td>
    <td align="left">timestamp with time zone</td>
    <td align="left">default now()</td>
  </tr>
  <tr valign="top">
    <td align="left">id</td>
    <td align="left">integer</td>
    <td align="left">not null default nextval('articles_id_seq'::regclass)</td>
  </tr>
</table>

### Table: Authors
<table border="1">
  <tr>
    <th align="center">Column</th>
    <th align="center">Type</th>
    <th align="center">Modifiers</th>
  </tr>
  <tr valign="top">
    <td align="left">name</td>
    <td align="left">text</td>
    <td align="left">not null</td>
  </tr>
  <tr valign="top">
    <td align="left">bio</td>
    <td align="left">text</td>
    <td align="left">&nbsp; </td>
  </tr>
  <tr valign="top">
    <td align="left">id</td>
    <td align="left">integer</td>
    <td align="left">not null default nextval('authors_id_seq'::regclass)</td>
  </tr>
</table>

### Table: Log
<table border="1">
  <tr>
    <th align="center">Column</th>
    <th align="center">Type</th>
    <th align="center">Modifiers</th>
  </tr>
  <tr valign="top">
    <td align="left">path</td>
    <td align="left">text</td>
    <td align="left">&nbsp; </td>
  </tr>
  <tr valign="top">
    <td align="left">ip</td>
    <td align="left">inet</td>
    <td align="left">&nbsp; </td>
  </tr>
  <tr valign="top">
    <td align="left">method</td>
    <td align="left">text</td>
    <td align="left">&nbsp; </td>
  </tr>
  <tr valign="top">
    <td align="left">status</td>
    <td align="left">text</td>
    <td align="left">&nbsp; </td>
  </tr>
  <tr valign="top">
    <td align="left">time</td>
    <td align="left">timestamp with time zone</td>
    <td align="left">default now()</td>
  </tr>
  <tr valign="top">
    <td align="left">id</td>
    <td align="left">integer</td>
    <td align="left">not null default nextval('log_id_seq'::regclass)</td>
  </tr>
</table>








## Future Improvements
- Right now the reports are only shown in command line, showing these reports in a more visual way in html would be very useful for the end user
- Hosting the SQL database on a public server would make testing this tool much more accessable