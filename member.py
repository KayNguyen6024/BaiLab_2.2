class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
	# Implement các phương thức cho thao tác insert update delete select vào DB
    def add_member(self, db):
        query = "INSERT INTO members (name) VALUES (%s)"
        db.execute_query(query, (self.name,))
		print(f"Đã thêm thành viên: '{self.name} với ID là {db.cursor.lastrowid}'")
	
    def delete_member(self, db):
        query = "DELETE FROM members WHERE member_id = %s"
        db.execute_query(query, (self.member_id,))
        
    def update_member_info(self, db):
        query = "UPDATE members SET name = %s WHERE member_id = %s"
        params = (self.name, self.member_id)
        db.execute_query(query, params)
    @staticmethod
    def search_member(db, member_id):
        query = "SELECT * FROM members WHERE member_id = %s"
        result = db.fetch_one(query, (member_id,))
        if result:
            return Member(result[0], result[1])
        else:
            return None

    @staticmethod
    def get_all_members(db):
        query = "SELECT * FROM members"
        return db.fetch_all(query)

