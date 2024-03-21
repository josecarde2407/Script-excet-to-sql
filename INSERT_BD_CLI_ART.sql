create database Bd_Datos;
use Bd_Datos;

CREATE TABLE `Bd_Datos`.`cli_art` (
  `id` int(50) NOT NULL,
  `n_articulo` VARCHAR(50) NULL,
  `des_articulo` VARCHAR(200) NULL,
  `un_negocio` VARCHAR(50) NULL,
  `udm` VARCHAR(10) NULL,
  `desfamilia` VARCHAR(100) NULL,
  `dessubfamilia` VARCHAR(100) NULL,
  `un_cliente` VARCHAR(50) NULL,
  `cliente` VARCHAR(50) NULL,
  PRIMARY KEY (`id`));
  
select * from cli_art;

