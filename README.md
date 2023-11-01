# FileDatabase

# About

## BNF

```BNF
<sql-statement> ::= <select-statement> | <insert-statement> | <update-statement> | <delete-statement>
<select-statement> ::= SELECT <select-list> FROM <table-list> [WHERE <search-condition>] [ORDER BY <order-list>]
<insert-statement> ::= INSERT INTO <table-name> [(<column-list>)] VALUES (<value-list>)
<update-statement> ::= UPDATE <table-name> SET <assignment-list> [WHERE <search-condition>]
<delete-statement> ::= DELETE FROM <table-name> [WHERE <search-condition>]
<select-list> ::= * | <column-name> [, <column-name>]*
<table-list> ::= <table-name> [, <table-name>]*
<search-condition> ::= <boolean-expression>
<order-list> ::= <order-item> [, <order-item>]*
<table-name> ::= <identifier>
<column-name> ::= <identifier>
<value-list> ::= <value-expression> [, <value-expression>]*
<assignment-list> ::= <assignment-item> [, <assignment-item>]*
<order-item> ::= <column-name> [ASC | DESC]
<identifier> ::= <letter> [<letter> | <digit>]*
<boolean-expression> ::= ...
<value-expression> ::= ...
<assignment-item> ::= ...

```
