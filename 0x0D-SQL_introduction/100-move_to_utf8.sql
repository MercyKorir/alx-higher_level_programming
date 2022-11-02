-- This script converts hbtn_0c_0 to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE first_table CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE first_table
MODIFY name utf8 COLLATE utf8_general_ci;
