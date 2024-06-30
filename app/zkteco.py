import base64
import string
from zk import ZK, const



def addUser(ip, port,password, uid, name,upassword, privilege, group_id, user_id):
    conn = None
    zk = ZK(ip, port=port, timeout=5, password=password, force_udp=False, ommit_ping=False)
    try:
        if privilege == 'Admin':
            privilege = const.USER_ADMIN
        else :
            privilege = const.USER_DEFAULT
        if name=="":
            return False, f"Name is required"
        if upassword is None:
           upassword = ''
        if group_id is None:
            group_id = ''
        # connect to device
        conn = zk.connect()
        # disable device, this method ensures no activity on the device while the process is run
        conn.disable_device()
        #Add User
        conn.set_user(uid=int(uid), name=name, privilege=const.USER_DEFAULT, password=upassword, user_id=str(user_id), group_id=group_id) 
        # enable device
        conn.test_voice()
        conn.enable_device()
        return True, f"User {name} added successfully"
    except Exception as e:
        return False, f"Error adding user {name} to device {ip}: {e}"
    finally:
        if conn:
            conn.disconnect()
            print(f"Disconnected from device {ip}")
            


def enrollFingerprintFromReader(ip, port, password, uid, temp_id):
    conn = None
    zk = ZK(ip, port=port, timeout=5, password=password, force_udp=False, ommit_ping=False)
    try:
        # connect to device
        conn = zk.connect()
        # disable device, this method ensures no activity on the device while the process is run
        conn.disable_device()
        # another commands will be here!
        # Add Fingerprint
        
        # Get Users from device
        users = conn.get_users()
        # Check if user exists
        if not users:
            return False, f"User {uid} not found on device {ip}"
        else:
            user_exists = False
            for user in users:
                if user.uid == int(uid):
                    user_exists = True
                    break
            if not user_exists:
                return False, f"User {uid} not found on device {ip}"
    
        

        # if
        temp_id = int(temp_id)
        if temp_id < 1 or temp_id > 10:
            return False, "Fingerprint ID must be between 1 and 10"
        conn.enroll_user(uid=int(uid),temp_id=int(temp_id))
        conn.enable_device()
        conn.test_voice()

        return True, f"Fingerprint {temp_id} added successfully"
    except Exception as e:
        return False, f"Error adding fingerprint {temp_id} to user {uid} on device {ip}: {e}"
    finally:
        if conn:
            conn.disconnect()
            print(f"Disconnected from device {ip}")


def enrollFaceFromReader(ip, port, password, uid):
    conn = None
    zk = ZK(ip, port=port, timeout=10, password=password, force_udp=False, ommit_ping=False,verbose=False)
    try:
        # connect to device
        conn = zk.connect()
        # disable device, this method ensures no activity on the device while the process is run
        conn.disable_device()
        # another commands will be here!
        # Add Fingerprint
         # Get Users from device
        users = conn.get_users()
        # Check if user exists
        if not users:
            return False, f"User {uid} not found on device {ip}"
        else:
            user_exists = False
            for user in users:
                if user.uid == int(uid):
                    user_exists = True
                    break
            if not user_exists:
                return False, f"User {uid} not found on device {ip}"
            
        conn.enroll_user(uid=int(uid),temp_id=111)
        conn.enable_device()
        conn.test_voice()

        return True, f"Face data added successfully"
    except Exception as e:
        return False, f"Error adding face data to user {uid} on device {ip}: {e}"
    finally:
        if conn:
            conn.disconnect()
            print(f"Disconnected from device {ip}")
    

def getAttendance(ip, port, password):
    conn = None
    zk = ZK(ip, port=port, timeout=5, password=password, force_udp=False, ommit_ping=False)
    try:
        # connect to device
        conn = zk.connect()
        # disable device, this method ensures no activity on the device while the process is run
        conn.disable_device()
        # another commands will be here!
        # Get Attendance
        rawAttendance = conn.get_attendance()
        conn.enable_device()
        
        attendance = []
        for att in rawAttendance:
            attendance.append({
                "user_id": att.user_id,
                "timestamp": att.timestamp,
                "status": att.status,               
            })
        return True, attendance
    except Exception as e:
        return False, f"Error getting attendance from device {ip}: {e}"
    finally:
        if conn:
            conn.disconnect()
            print(f"Disconnected from device {ip}")
            
def clearAttendance(ip, port, password):
    conn = None
    zk = ZK(ip, port=port, timeout=5, password=password, force_udp=False, ommit_ping=False)
    try:
        # connect to device
        conn = zk.connect()
        # disable device, this method ensures no activity on the device while the process is run
        conn.disable_device()
        # another commands will be here!
        # Clear Attendance
        conn.clear_attendance()
        conn.enable_device()
        return True, "Attendance cleared successfully"
    except Exception as e:
        return False, f"Error clearing attendance from device {ip}: {e}"
    finally:
        if conn:
            conn.disconnect()
            print(f"Disconnected from device {ip}")
                
            
def getUsers(ip, port, password):
    conn = None
    zk = ZK(ip, port=port, timeout=5, password=password, force_udp=False, ommit_ping=False)
    try:
        # connect to device
        conn = zk.connect()
        # disable device, this method ensures no activity on the device while the process is run
        conn.disable_device()
        # another commands will be here!
        # Get Users from Device raw
        rawusers = conn.get_users()
        # Enable device
        conn.enable_device()
        # Parse Users
        users = []
        for user in rawusers:
            privilege = 'User'
            if user.privilege == const.USER_ADMIN:
                privilege = 'Admin'
            if isinstance(user.name, bytes):
                user_name = base64.b64decode(user.name).decode('utf-8', errors='replace')
            else:
                user_name = user.name  # If already a string, use it directly
                # Decode the Base64 encoded string
            # user_name_str = user.name.decode('utf-8')
            # user_name = base64.b64decode(user_name_str)

            # Convert bytes to string
            # user_name_str = user.name.decode('utf-8')  # Assuming 'utf-8' encoding
            # user_name = base64.b64decode(user_name_str).decode('utf-8')  # Decode from Base64 and then decode to string

            users.append({
                'uid': user.uid,
                'name': user_name,
                'privilege': privilege,
                'password': user.password,
                'group_id': user.group_id,
                'user_id': user.user_id,
            })
            
     
        return True, users
    except Exception as e:
        return False, f"Error getting users from device {ip}: {e}"
    finally:
        if conn:
            conn.disconnect()
            print(f"Disconnected from device {ip}")
            
def deleteUser(ip, port, password, uid):
    conn = None
    zk = ZK(ip, port=port, timeout=5, password=password, force_udp=False, ommit_ping=False)
    try:
        # connect to device
        conn = zk.connect()
        # disable device, this method ensures no activity on the device while the process is run
        conn.disable_device()
        # another commands will be here!
        # Delete User
        conn.delete_user(uid)
        conn.enable_device()
        conn.test_voice()

        return True, f"User {uid} deleted successfully"
    except Exception as e:
        return False, f"Error deleting user {uid} from device {ip}: {e}"
    finally:
        if conn:
            conn.disconnect()
            print(f"Disconnected from device {ip}")
            
def deleteFingerprint(ip, port, password, uid, fid):
    conn = None
    zk = ZK(ip, port=port, timeout=5, password=password, force_udp=False, ommit_ping=False)
    try:
        # connect to device
        conn = zk.connect()
        # disable device, this method ensures no activity on the device while the process is run
        conn.disable_device()
        # another commands will be here!
        # Delete Fingerprint
        conn.delete_user_template(uid, fid)
        conn.enable_device()
        return True, f"Fingerprint {fid} deleted successfully"
    except Exception as e:
        return False, f"Error deleting fingerprint {fid} from user {uid} on device {ip}: {e}"
    finally:
        if conn:
            conn.disconnect()
            print(f"Disconnected from device {ip}")