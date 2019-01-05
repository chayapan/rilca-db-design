This is SQL for MySQL 5.7:

<pre>
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema rilca_pa
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema rilca_pa
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `rilca_pa` DEFAULT CHARACTER SET utf8 ;
USE `rilca_pa` ;

-- -----------------------------------------------------
-- Table `rilca_pa`.`pa_items`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rilca_pa`.`pa_items` (
  `item_id` INT NOT NULL,
  `level` VARCHAR(45) NOT NULL,
  `parent` INT NULL,
  `display_rank` INT NULL,
  `item_number` VARCHAR(45) NULL,
  `score_points` VARCHAR(45) NULL,
  `section_number` VARCHAR(45) NULL,
  `description_th` VARCHAR(500) NULL,
  `description_en` VARCHAR(500) NULL,
  `hint_th` VARCHAR(500) NULL,
  `hint_en` VARCHAR(500) NULL,
  PRIMARY KEY (`item_id`),
  CONSTRAINT `parent_id`
    FOREIGN KEY (`item_id`)
    REFERENCES `rilca_pa`.`pa_items` (`parent`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rilca_pa`.`staffs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rilca_pa`.`staffs` (
  `staff_id` INT NOT NULL,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  PRIMARY KEY (`staff_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rilca_pa`.`academic_staff`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rilca_pa`.`academic_staff` (
  `staff_id` INT NOT NULL,
  `program_id` VARCHAR(45) NULL,
  `rank` VARCHAR(45) NULL,
  PRIMARY KEY (`staff_id`),
  CONSTRAINT `fk_academic_staff_staffs1`
    FOREIGN KEY (`staff_id`)
    REFERENCES `rilca_pa`.`staffs` (`staff_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rilca_pa`.`academic_program`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rilca_pa`.`academic_program` (
  `program_id` INT NOT NULL,
  PRIMARY KEY (`program_id`),
  CONSTRAINT `fk_academic_program_academic_staff1`
    FOREIGN KEY (`program_id`)
    REFERENCES `rilca_pa`.`academic_staff` (`staff_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rilca_pa`.`pa_documents`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rilca_pa`.`pa_documents` (
  `document_id` INT NOT NULL,
  `staff_id` INT NULL,
  `program_id` INT NULL,
  `document_number` VARCHAR(45) NULL,
  `fiscal_year` VARCHAR(45) NULL,
  `submit_date` DATETIME NULL,
  `approve_date` DATETIME NULL,
  `period_start` DATE NULL,
  `period_end` DATE NULL,
  `review_date` DATETIME NULL,
  `score_date` DATETIME NULL,
  `accept_date` DATETIME NULL,
  `status` VARCHAR(45) NULL,
  PRIMARY KEY (`document_id`),
  INDEX `fk_pa_documents_academic_program1_idx` (`program_id` ASC),
  INDEX `fk_pa_documents_staffs1_idx` (`staff_id` ASC),
  CONSTRAINT `program_id`
    FOREIGN KEY (`program_id`)
    REFERENCES `rilca_pa`.`academic_program` (`program_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `staff_id`
    FOREIGN KEY (`staff_id`)
    REFERENCES `rilca_pa`.`staffs` (`staff_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rilca_pa`.`pa_lines`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rilca_pa`.`pa_lines` (
  `line_id` INT NOT NULL,
  `program_id` INT NULL,
  `document_id` INT NULL,
  `line_number` VARCHAR(45) NULL,
  `item_id` INT NULL,
  `description_th` VARCHAR(500) NULL,
  `description_en` VARCHAR(500) NULL,
  `specific_details` VARCHAR(500) NULL,
  `score_plan` DECIMAL(3,2) NULL,
  `score_actual` DECIMAL(3,2) NULL,
  `score_deadline` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `status` VARCHAR(45) NULL,
  PRIMARY KEY (`line_id`),
  INDEX `document_id_idx` (`document_id` ASC),
  INDEX `item_id_idx` (`item_id` ASC),
  INDEX `academic_program_idx` (`program_id` ASC),
  CONSTRAINT `fk_pa_lines_document_id`
    FOREIGN KEY (`document_id`)
    REFERENCES `rilca_pa`.`pa_documents` (`document_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pa_lines_item_id`
    FOREIGN KEY (`item_id`)
    REFERENCES `rilca_pa`.`pa_items` (`item_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pa_lines_program_id`
    FOREIGN KEY (`program_id`)
    REFERENCES `rilca_pa`.`academic_program` (`program_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rilca_pa`.`executive`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rilca_pa`.`executive` (
  `staff_id` INT NOT NULL,
  `position` VARCHAR(45) NULL,
  PRIMARY KEY (`staff_id`),
  CONSTRAINT `fk_executives_staffs1`
    FOREIGN KEY (`staff_id`)
    REFERENCES `rilca_pa`.`staffs` (`staff_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rilca_pa`.`pa_approvals`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rilca_pa`.`pa_approvals` (
  `approve_id` INT NOT NULL,
  `document_id` INT NULL,
  `executive_id` INT NULL,
  `approve_date` DATE NULL,
  `update_by` INT NULL,
  `status` VARCHAR(45) NULL,
  PRIMARY KEY (`approve_id`),
  INDEX `fk_pa_approvals_pa_documents1_idx` (`document_id` ASC),
  INDEX `fk_pa_approvals_executive1_idx` (`executive_id` ASC),
  CONSTRAINT `fk_pa_approvals_pa_documents1`
    FOREIGN KEY (`document_id`)
    REFERENCES `rilca_pa`.`pa_documents` (`document_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pa_approvals_executive1`
    FOREIGN KEY (`executive_id`)
    REFERENCES `rilca_pa`.`executive` (`staff_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rilca_pa`.`support_staff`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rilca_pa`.`support_staff` (
  `staff_id` INT NOT NULL,
  `position` VARCHAR(45) NULL,
  `pa_approvals_approve_id` INT NOT NULL,
  PRIMARY KEY (`staff_id`, `pa_approvals_approve_id`),
  INDEX `fk_support_staff_pa_approvals1_idx` (`pa_approvals_approve_id` ASC),
  CONSTRAINT `fk_support_staffs_staffs1`
    FOREIGN KEY (`staff_id`)
    REFERENCES `rilca_pa`.`staffs` (`staff_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_support_staff_pa_approvals1`
    FOREIGN KEY (`pa_approvals_approve_id`)
    REFERENCES `rilca_pa`.`pa_approvals` (`approve_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

</pre>
