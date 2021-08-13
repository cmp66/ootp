use pt;

alter table playerstats add column woba FLOAT NULL DEFAULT 0;
alter table playerstats add column wrcplus FLOAT NULL DEFAULT 0;
alter table playerstats add column babip FLOAT NULL DEFAULT 0;
alter table playerstats add column kminuswalk FLOAT NULL DEFAULT 0;
alter table playerstats add column fip FLOAT NULL DEFAULT 0;
alter table playerstats add column opsplus FLOAT NULL DEFAULT 0;
alter table playerstats add column whip FLOAT NULL DEFAULT 0;

update playerstats set woba=0.0 where woba=NULL;
update playerstats set wrcplus=0.0 where wrcplus=NULL;
update playerstats set babip=0.0 where babip=NULL;
update playerstats set kminuswalk=0.0 where kminuswalk=NULL;
update playerstats set fip=0.0 where fip=NULL;
update playerstats set opsplus=0.0 where opsplus=NULL;
update playerstats set whip=0.0 where whip=NULL;
