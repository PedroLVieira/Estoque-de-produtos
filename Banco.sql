CREATE TABLE `banco`.`produtos` (
  `idProdutos` INT NOT NULL AUTO_INCREMENT,
  `NomeProduto` VARCHAR(45) NOT NULL,
  `PrecoProd` DOUBLE NOT NULL,
  `quantidade` INT NOT NULL,
  PRIMARY KEY (`idProdutos`),
  UNIQUE INDEX `idProdutos_UNIQUE` (`idProdutos` ASC) VISIBLE);
