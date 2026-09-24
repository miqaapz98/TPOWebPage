create database bikes;

create table Bicicletas(
id_Bici varchar(5) not null primary key,
tipo_Bici varchar(15) not null ,
rodado int (2) not null,
marca varchar(10) not null,
descripcion varchar(20) not null,
precio double(8,2) not null);

create table Ventas(
id_Venta int(4) not null,
dni int(8) not null primary key,
nombre varchar(32) not null,	
apellido varchar(32) not null,
telef varchar(10)not null,
cod_Bici varchar(5) not null,	
fecha_Venta date not null,
precio double(8,2) not null
);
alter table Ventas add foreign key (cod_Bici) references Bicicletas (id_Bici);

insert into Bicicletas (id_Bici,tipo_Bici,rodado,marca,Descripcion,precio) values
('BM3','BMX',20,'Halley','Freestyle alumino',33000),
('MB21','Mountain',26,'Fire bird','aluminio MN 21V',43900),
('MB25','Mountain',27,'Raleigh','260 21V',78230),
('PL2','Plegable',20,'Raleigh','Curvada Plegable',62530),
('PS45','Playera',26,'OLMO','Amelie Paseo',56234);
