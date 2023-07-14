-- SELECT * FROM `pris`.`pris_region` LIMIT 100;
-- TRUNCATE TABLE `pris`.`pris_country`;
-- ALTER TABLE `pris`.`pris_country` MODIFY COLUMN country VARCHAR(50);

-- ALTER TABLE `pris`.`pris_type`
-- ADD COLUMN `country` VARCHAR(50) AFTER `type`;

USE pris;
SELECT COUNT(*) AS row_count FROM pris_age;
SELECT COUNT(*) AS row_count FROM pris_country;
SELECT COUNT(*) AS row_count FROM pris_region;
SELECT COUNT(*) AS row_count FROM pris_trend;
SELECT COUNT(*) AS row_count FROM pris_type;
