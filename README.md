# Web Site Performance Metrics Reporter

## Intro
The goal of this project is to practise my SQL (PostgreSQL) and Python skills by generaing performance reports for a fictional Web News site.

## To use
Run one of the following methods from App module.

### Reports

### What are the most popular three articles of all time?
Which articles have been accessed the most? Information is presented as a sorted list with the most popular articles at the top.

#### Example:
`338647 views --- 'Candidate is jerk, alleges rival'`

`253801 views --- 'Bears love berries, alleges bear'`


### Who are the most popular article authors of all time? 
That is, which authors has the most page views? Presented  as a sorted list with the most viewed author at the top.

#### Example:

`Markoff Chaney --- 84557 views`
`Anonymous Contributor --- 170098 views`
`Rudolf von Treppenwitz --- 423457 views`

### On which days did more than 1% or more of web requests lead to errors? 

#### Example:

`day: 2016-07-17 --- Error percent: 2.26%`

## Files
- App.py: Provides three methods each of which print a type of report.

##Technology
- Databse:
  - SQL: PostgreSQL(v9.5.10)

Python Version: 2.7

Virtual Machine: vangres/virtual box

## Database Structure
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

### View: Article to Log
This establishes the referance between article web page URL and resposective article ID.

<table border="1">
  <tr>
    <th align="center">Column</th>
    <th align="center">Type</th>
    <th align="center">Modifiers</th>
  </tr>
  <tr valign="top">
    <td align="left">article_id</td>
    <td align="left">integer</td>
    <td align="left">&nbsp; </td>
  </tr>
  <tr valign="top">
    <td align="left">slug_derived_from_url</td>
    <td align="left">text</td>
    <td align="left">&nbsp; </td>
  </tr>
  <tr valign="top">
    <td align="left">log_id</td>
    <td align="left">integer</td>
    <td align="left">&nbsp; </td>
  </tr>
</table>

The SQL query used to generate this view may be seen in [article_to_log_view.sql](./Queries/article_to_log_view.sql)

## Future Improvements
- Right now the reports are only shown in command line, showing these reports in a more visual way in html would be very useful for the end user
- Hosting the SQL database on a public server would make testing this tool much more accessable
- save the reports as views and serve them on request from a web server