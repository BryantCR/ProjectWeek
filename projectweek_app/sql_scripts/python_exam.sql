-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema python_exam
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema python_exam
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `python_exam` DEFAULT CHARACTER SET utf8 ;
USE `python_exam` ;

-- -----------------------------------------------------
-- Table `python_exam`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `python_exam`.`users` (
  `users_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `users_password` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`users_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `python_exam`.`cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `python_exam`.`cars` (
  `cars_id` INT NOT NULL AUTO_INCREMENT,
  `car_name` VARCHAR(45) NOT NULL,
  `car_make` VARCHAR(45) NOT NULL,
  `car_description` VARCHAR(255) NOT NULL,
  `car_seller` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `car_price` FLOAT NOT NULL,
  `car_year` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`cars_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `python_exam`.`users_cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `python_exam`.`users_cars` (
  `users_cars_id` INT NOT NULL AUTO_INCREMENT,
  `users_users_id` INT NOT NULL,
  `cars_cars_id` INT NOT NULL,
  PRIMARY KEY (`users_cars_id`, `users_users_id`, `cars_cars_id`),
  INDEX `fk_users_has_cars_cars1_idx` (`cars_cars_id` ASC) VISIBLE,
  INDEX `fk_users_has_cars_users_idx` (`users_users_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_cars_users`
    FOREIGN KEY (`users_users_id`)
    REFERENCES `python_exam`.`users` (`users_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_cars_cars1`
    FOREIGN KEY (`cars_cars_id`)
    REFERENCES `python_exam`.`cars` (`cars_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


/*************************************************************************************/
select *
from cars;

select *
from users_cars;

SELECT users.users_id, users.first_name, cars.car_name, cars.car_year, cars.car_seller FROM cars JOIN users_cars ON cars.cars_id = users_cars.cars_cars_id JOIN users ON users.users_id = users_cars.users_users_id;












