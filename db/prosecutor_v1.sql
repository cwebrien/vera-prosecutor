CREATE TABLE `veraprosecutor.prosecutor` (
	state          varchar(32)    NOT NULL,
	district       varchar(128)   NOT NULL,
	name           varchar(128)   NOT NULL,
	email          varchar(128)   NULL,
	phone          varchar(16)    NULL,
	website        varchar(128)   NULL,
	election_year  int			  NULL,
	party          varchar(16)    NULL,
	terms_served   int            NULL,
	PRIMARY KEY    (state, district, name)
);
