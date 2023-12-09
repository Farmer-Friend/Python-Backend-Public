from responses import (
    method_not_allowed_response,
    internal_server_error_response,
    missing_parameters_response,
    unauthorized_response,
    mysql_connection_error_response,
    item_details_not_found_response,
    success_response
)

from Databases.mySQL import connectToDB,checkSession

def deleteProduct(eventMethod,eventBoody):
    try:

        if eventMethod !='POST':
            return method_not_allowed_response
        

        sessionToken=eventBoody.get('sessionToken')
        productID=eventBoody.get('productID')

        if sessionToken==None or productID==None:
            return missing_parameters_response
        

        user_id=checkSession(sessionToken)
        if not user_id:
            return unauthorized_response
        
        conn=connectToDB()
        if not conn:
            return mysql_connection_error_response
        
        cursor=conn.cursor()
        cursor.execute("SELECT owner_id FROM Product WHERE product_id=?", (productID,))
        owner_id = cursor.fetchone()

        if owner_id==None:
            return item_details_not_found_response
        
        if owner_id[0]!=user_id:
            return unauthorized_response
        
        cursor.execute("DELETE FROM Product WHERE product_id=?", (productID,))

        # Insert into transaction
        cursor.execute(
            "INSERT INTO transactions (user_id,action) VALUES (?, 'delete')",
            (user_id)
        )

        conn.commit()
        return success_response
    
    except Exception as e:
        return internal_server_error_response