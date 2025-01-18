import psycopg2
from config import DB_HOST, DB_NAME_1, DB_NAME_2, DB_USER, DB_PASSWORD, DB_PORT
from psycopg2.extras import DictCursor

def get_data_from_db_1_table_movies(query):
    """
    Hàm này kết nối đến PostgreSQL, thực thi truy vấn và trả về dữ liệu dưới dạng danh sách.

    :param query: Câu lệnh SQL để thực thi
    :return: List chứa các bản ghi kết quả từ truy vấn
    """
    try:
        # Kết nối đến cơ sở dữ liệu PostgreSQL
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME_1,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        
        # Tạo con trỏ
        cursor = conn.cursor(cursor_factory=DictCursor)

        # Thực thi câu lệnh SQL
        cursor.execute(query)

        # Lấy tất cả các kết quả và chuyển thành list
        results = cursor.fetchall()

        # Trả về dữ liệu dưới dạng list
        return results

    except Exception as e:
        print(f"Lỗi khi kết nối hoặc truy vấn: {e}")
        return []

    finally:
        # Đóng kết nối và con trỏ
        if conn:
            cursor.close()
            conn.close()
            
def get_data_from_db_2_table_movies(query):
    """
    Hàm này kết nối đến PostgreSQL, thực thi truy vấn và trả về dữ liệu dưới dạng danh sách.

    :param query: Câu lệnh SQL để thực thi
    :return: List chứa các bản ghi kết quả từ truy vấn
    """
    try:
        # Kết nối đến cơ sở dữ liệu PostgreSQL
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME_2,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        
        # Tạo con trỏ
        cursor = conn.cursor(cursor_factory=DictCursor)

        # Thực thi câu lệnh SQL
        cursor.execute(query)

        # Lấy tất cả các kết quả và chuyển thành list
        results = cursor.fetchall()

        # Trả về dữ liệu dưới dạng list
        return results

    except Exception as e:
        print(f"Lỗi khi kết nối hoặc truy vấn: {e}")
        return []

    finally:
        # Đóng kết nối và con trỏ
        if conn:
            cursor.close()
            conn.close()
def get_data_from_db_2_table_reviews(query):
    """
    Hàm này kết nối đến PostgreSQL, thực thi truy vấn và trả về dữ liệu dưới dạng danh sách.

    :param query: Câu lệnh SQL để thực thi
    :return: List chứa các bản ghi kết quả từ truy vấn
    """
    try:
        # Kết nối đến cơ sở dữ liệu PostgreSQL
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME_2,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        
        # Tạo con trỏ
        cursor = conn.cursor(cursor_factory=DictCursor)

        # Thực thi câu lệnh SQL
        cursor.execute(query)

        # Lấy tất cả các kết quả và chuyển thành list
        results = cursor.fetchall()

        # Trả về dữ liệu dưới dạng list
        return results

    except Exception as e:
        print(f"Lỗi khi kết nối hoặc truy vấn: {e}")
        return []

    finally:
        # Đóng kết nối và con trỏ
        if conn:
            cursor.close()
            conn.close()
