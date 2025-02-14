-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `wolftrack_se` DEFAULT CHARACTER SET utf8 ;
USE `wolftrack_se` ;
-- -----------------------------------------------------
-- Table `wolftrack_se`.`user_login`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wolftrack_se`.`user_login` ;

CREATE TABLE IF NOT EXISTS `wolftrack_se`.`user_login` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`user_id`))
ENGINE = InnoDB;
-- -----------------------------------------------------
-- Table `wolftrack_se`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wolftrack_se`.`user` ;

CREATE TABLE IF NOT EXISTS `wolftrack_se`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `full_name` VARCHAR(45) NOT NULL,
  `linkedin_link` VARCHAR(45) NULL,
  `github_link` VARCHAR(45) NULL,
  `profile_link` VARCHAR(45) NULL,
  `gender` VARCHAR(45) NULL,
  `location` VARCHAR(75) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  UNIQUE INDEX `first_name_UNIQUE` (`full_name` ASC) VISIBLE,
  FOREIGN KEY (`user_id`)
    REFERENCES `wolftrack_se`.`user_login` (`user_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `wolftrack_se`.`company`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wolftrack_se`.`company` ;

CREATE TABLE IF NOT EXISTS `wolftrack_se`.`company` (
  `company_id` INT NOT NULL AUTO_INCREMENT,
  `company_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`company_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `wolftrack_se`.`roles`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wolftrack_se`.`roles` ;

CREATE TABLE IF NOT EXISTS `wolftrack_se`.`roles` (
  `role_id` INT NOT NULL AUTO_INCREMENT,
  `role` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`role_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `wolftrack_se`.`application`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wolftrack_se`.`application` ;

CREATE TABLE IF NOT EXISTS `wolftrack_se`.`application` (
  `application_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `company_id` INT NOT NULL,
  `role_id` INT NOT NULL,
  `application_date` TIMESTAMP NOT NULL,
  `job_description` VARCHAR(100) NULL,
  `salary` FLOAT NULL,
  `location` VARCHAR(45) NOT NULL,
  `imortant_links` VARCHAR(45) NULL,
  `recruiter_id` INT,
  `due_date` DATETIME,
  `status` ENUM("TO_DO", "APPLIED", "IN_PROCESS", "ACCEPTED", "DECLINED") NOT NULL,
  PRIMARY KEY (`application_id`),
  INDEX `user_id_idx` (`user_id` ASC) VISIBLE,
  INDEX `role_id_idx` (`role_id` ASC) VISIBLE,
  INDEX `company_id_idx` (`company_id` ASC) VISIBLE,
    FOREIGN KEY (`user_id`)
    REFERENCES `wolftrack_se`.`user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    FOREIGN KEY (`role_id`)
    REFERENCES `wolftrack_se`.`roles` (`role_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    FOREIGN KEY (`company_id`)
    REFERENCES `wolftrack_se`.`company` (`company_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
