-- DELIMITER: 묶어주는 개념
DELIMITER //
CREATE PROCEDURE myProc()
BEGIN
SELECT * FROM member WHERE member_name = "나훈아";
SELECT * FROM item WHERE product_name = "삼각김밥";
END //
DELIMITER ;

-- 호출 
CALL myProc()