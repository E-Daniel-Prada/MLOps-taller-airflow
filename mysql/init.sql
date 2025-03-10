CREATE TABLE penguins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    species VARCHAR(50) NOT NULL,
    island VARCHAR(50) NOT NULL,
    bill_length_mm FLOAT,
    bill_depth_mm FLOAT,
    flipper_length_mm FLOAT,
    body_mass_g INT,
    sex VARCHAR(10)
);

CREATE TABLE penguins_preprocessed (
    id INT AUTO_INCREMENT PRIMARY KEY,
    species VARCHAR(50) NOT NULL,
    island VARCHAR(50) NOT NULL,
    bill_length_mm FLOAT,
    bill_depth_mm FLOAT,
    flipper_length_mm FLOAT,
    body_mass_g INT,
    sex VARCHAR(10)
);
