import mysql.connector as mc
import streamlit as st
import pandas as pd
from PIL import Image
import base64

# Connect to the database
mydb = mc.connect(host="localhost", user="root", password="K]es/Y,)#d=s7RH22&Q8", database="hosp_recs")
mycursor = mydb.cursor()
print("Connect established")


# Set the page configuration (optional)
st.set_page_config(page_title="My App", page_icon=":sparkles:", layout="wide")

# Function to load a GIF image and convert it to base64
def load_gif(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Load the GIF image and convert it to base64
gif_path = r"C:\\Users\\p_nag\\Downloads\\beating-heart-gif.gif"  # Path to your GIF file
gif_base64 = load_gif(gif_path)

# Add CSS for background GIF
st.markdown(
    f"""
    <style>
        .stApp {{
            background-image: url(data:image/gif;base64,{gif_base64});  /* Base64 encoded GIF */
            background-size: cover;  /* Cover the entire area */
            background-repeat: no-repeat;  /* No repeating */
            background-attachment: fixed;  /* Fix the background when scrolling */
            background-position: center;  /* Center the image */
            height: 100vh;  /* Set height to 100% of the viewport */
        }}
    </style>
    """,
    unsafe_allow_html=True
)
def main():
    # Initialize session state attributes
    if 'index' not in st.session_state:
        st.session_state.index = 0
    if 'signedout' not in st.session_state:
        st.session_state.signedout = True
    if 'user_type' not in st.session_state:
        st.session_state.user_type = "Select"
    if 'doctorsignedout' not in st.session_state:
        st.session_state.doctorsignedout = True
    if 'showtable' not in st.session_state:
        st.session_state.showtable = False
    if 'showbox' not in st.session_state: 
        st.session_state.showbox = True
    if 'patient' not in st.session_state: 
        st.session_state.patient = False
    if 'userdisplay' not in st.session_state: 
        st.session_state.userdisplay = True


    # Define the function to create a slideshow with navigation arrows
    def display_slideshow(images):
        # Initialize session state for the current index if not already set
        if 'image_index' not in st.session_state:
            st.session_state.image_index = 0
        
        # Display the current image
        st.image(images[st.session_state.image_index], use_column_width=True)
        
        # Navigation buttons
        col1, col2, col3 = st.columns([1, 6, 1])  # Create three columns: for previous, next, and empty space

        with col1:
            if st.button("Prev"):
                # Move to the previous image
                if st.session_state.image_index > 0:
                    st.session_state.image_index -= 1
                else:
                    st.session_state.image_index = len(images) - 1  # Loop to the last image

        with col2:
            st.empty()  # Empty space in the middle for centering the image

        with col3:
            text="Next"
            if st.button(text):
                # Move to the next image
                if st.session_state.image_index < len(images) - 1:
                    st.session_state.image_index += 1
                else:
                    st.session_state.image_index = 0  # Loop to the first image

    # Main application logic
    if st.session_state.signedout:
         
            # Create a container for the main content
        content = st.container()
            
            # Define the paths to your images
        image_paths = [
                "C:\\Users\\p_nag\\Downloads\\InsideChettinadHospital-removebg-preview.png",
                "C:\\Users\\p_nag\\Downloads\\2-removebg-preview.png",
                "C:\\Users\\p_nag\\Downloads\\3-removebg-preview.png",
                "C:\\Users\\p_nag\\Downloads\\4-removebg-preview.png",
                "C:\\Users\\p_nag\\Downloads\\5-removebg-preview.png",
                "C:\\Users\\p_nag\\Downloads\\6-removebg-preview.png",
                "C:\\Users\\p_nag\\Downloads\\7-removebg-preview.png",
                "C:\\Users\\p_nag\\Downloads\\8-removebg-preview.png"
            ]
            
            # Load images
        images = [Image.open(path) for path in image_paths]

            # Sidebar elements
        st.sidebar.image("C:\\Users\\p_nag\\Downloads\\Subheading_Pic_Final.png", caption="Believe in us", width=275)
        st.sidebar.title("Navigation")
        page = st.sidebar.radio("Go to", ["Home", "Admin", "Doctor", "About"])
        st.sidebar.write("<hr>", unsafe_allow_html=True)
        st.sidebar.write("<p style='text-align: center;'> Emergency: <br> 110 <br> Chettinad Helpline:<br> 1800 6780 </p>", unsafe_allow_html=True)

            # Display the slideshow in the main content area
        with content:
            if page=='Home':   
                st.markdown("<h1 style='text-align: center;'>Welcome to Chettinad Hospitals</h1>", unsafe_allow_html=True)
                st.markdown("<h3 style='text-align: center;'>This is an app to access records of Faculties And Patients.</h3>", unsafe_allow_html=True)
                display_slideshow(images)

        if page == "Admin": 
                st.write("Login to proceed further!")
                with st.form(key='admin_form'):

                    ad_id = st.text_input("Enter your Admin Username:")
                    ad_password = st.text_input("Enter your Admin Password:", type="password")
                    submit_button = st.form_submit_button("Submit")
                    if submit_button:
                        sql="select * from admin_login"
                        mycursor.execute(sql)
                        value=mycursor.fetchall()
                        flag=0
                        for i in value:
                            if i[1]==ad_id and i[2]==ad_password:
                                    print(i)
                                    st.success("You have logged in successfully! Please proceed.")
                                    st.session_state.username = ad_id
                                    st.session_state.signedout = False
                                    st.session_state.doctorsignedout = False
                                    st.session_state.user_type = "Admin"
                                    st.rerun()
                            else:
                                flag=1
                        if flag==1:
                             st.warning("Invalid Admin ID or Password!")
        
        global current_user
        if page == "Doctor":
                st.write("Login to proceed further!")
                with st.form(key='Actual_doctor_form'):
                    dc_id = st.text_input("Enter your Doctor Username:")
                    dc_password = st.text_input("Enter your Doctor Password:", type="password")
                    submit_button = st.form_submit_button("Submit")
                    if submit_button:
                        sql="select * from doctor_login"
                        mycursor.execute(sql)
                        value_dc=mycursor.fetchall()
                        print(value_dc)
                        flag=0
                        for i in value_dc:
                            print(i[0]==dc_id)
                            if i[0]==int(dc_id) and i[1]==dc_password:
                                    st.session_state.current_user = i  
                                    st.success("You have logged in successfully! Please proceed.")
                                    st.session_state.username = dc_id
                                    st.session_state.signedout = False
                                    st.session_state.doctorsignedout = True
                                    st.session_state.user_type = "Actual_Doctor"
                                    st.rerun()
                            else:
                                flag=1 

                        if flag==1:
                             st.warning("Invalid Doctor ID or Password!")
        if page == "About": 
            st.write("Hi! This software was coded by Kamesh and Karthik Nagendran of 12E, the logos and designing part was done by Harshavarshan devandra khanolkar, Arsh bharti helped us mentally and gave us ideas to design the software")           

    elif st.session_state.doctorsignedout:
      if 'current_user' in st.session_state:
        current_user = st.session_state.current_user
        st.header(f"Welcome, {current_user[2]}")
        st.markdown("Go below to execute a function!")

        # Create a two-column layout for "Previous" and "Signout" buttons
        col1, _, col2 = st.columns([1, 5, 1])  # The middle column is much wider to create space between the buttons
    
    
        with col2:
            signout_button = st.button('Signout', key="docsignout_button")
            if signout_button:
                st.session_state.username = ''
                st.session_state.user_type = "Select"
                st.session_state.doctorsignedout = False
                st.session_state.signedout = True
                st.session_state.userdisplay = True
                st.rerun()


        if st.session_state.user_type == 'Actual_Doctor':
                st.markdown(
                    """
                    <style>
                    div.streamlit-expanderHeader {
                    margin-bottom: 10px;
                    }
                    div[data-baseweb="tab-list"] button {
                        margin-right: 100px;  /* Adjust the spacing between tabs */
                        padding: 10px 20px;  /* Adjust the padding inside each tab */
                        font-size: 100px;     /* Adjust the font size */
                    }
                    </style>
                    """,
                    unsafe_allow_html=True
                )

                 #Check if current_user is stored in session state
                if 'current_user' in st.session_state:
                    current_user = st.session_state.current_user
                    #Print details of the logged-in user
                    st.write(f"Doctor Id: {current_user[0]}")
                    st.write(f"Name: {current_user[2]}")
                    st.write(f"Sex: {current_user[3]}")
                    st.write(f"Department:  {current_user[4]}")
                    st.write(f"Address:  {current_user[5]}")
                    st.write(f"Phone Number :  {current_user[6]}")
                    st.write(f"Email Id:  {current_user[7]}")
                    st.write(f"Date of Birth:  {current_user[8]}")
                    st.write(f"Joining Date:  {current_user[9]}")
                    st.write(f"Leaving Date:  {current_user[10]}")
                    st.write(f"Experience:  {current_user[11]}")
                    st.write(f"Religion:  {current_user[12]}")
                    st.write(f"Mother Tongue:  {current_user[13]}")
                    st.write(f"Nationality:  {current_user[14]}")
                    st.write(f"Blood Group:  {current_user[15]}")

                
                task = st.selectbox("**Select your task**",["Select", "Task Management" ,"Patient"])
                
                if task == "Task Management": 
                        tab1 , tab2, tab3, tab4 = st.tabs(["Assign", "Track", "Modify/Change", "Remove"])
                        with tab1:
                            with st.form(key="TMcreate_form", clear_on_submit=True):
                                st.subheader("Create Your Task!")
                                TM_ID=st.text_input("Enter Task ID: ")
                                TM_Task = st.text_input("Enter Your Task:")
                                TM_Desc = st.text_area("Enter brief Description of Task:")
                                TM_Time = st.time_input("Enter Time:")
                                TM_Status = st.text_area("Enter the current Status")
                                TM_Priority = st.selectbox("Enter Priority of the Task: ", ["High","Medium","Low"])
                                TM_DueDate = st.date_input("Enter Task Due Date: ")
                                TM_CompletionDate = st.date_input("Enter Completion Date:")
                                submit = st.form_submit_button("Create a Task")

                            if submit:
                                sql = "INSERT INTO TM (Task_ID,Task, Description, Time, Status, Priority, Due_Date,Completed_Date) VALUES (%s,%s, %s, %s, %s, %s, %s, %s)"
                                values = (TM_ID,TM_Task, TM_Desc, TM_Time, TM_Status, TM_Priority, TM_DueDate,TM_CompletionDate)
                                try:
                                    mycursor.execute(sql, values)
                                    mydb.commit()
                                    st.success("Successfully Created a Task")
                                except Exception as e:
                                    st.error(f"Failed to create a Task: {e}")
                            
                            with tab2:
                                st.subheader("Your tasks:")
                                sql = "SELECT * FROM TM"
                                mycursor.execute(sql)
                                data = mycursor.fetchall()

                                if len(data) == 0:
                                    st.write("No records found.")
                                else:
                                    html_table = """
                                    <style>
                                        .scrollable-table-container {
                                            max-height: 600px;
                                            overflow-y: auto;
                                        }
                                        table {
                                            width: 100%;  /* Smaller table width */
                                            border-collapse: collapse;
                                            margin: 25px auto;  /* Center the table */
                                            font-size: 14px;  /* Medium font size */
                                            text-align: left;
                                        }
                                        th, td {
                                            padding: 10px 12px;  /* Adjust padding */
                                        }
                                        th {
                                            background-color: #333;
                                            color: #ffffff;
                                        }
                                        tr:nth-child(even) {
                                            background-color: #777;
                                        }
                                        tr:nth-child(odd) {
                                            background-color: #555;
                                        }
                                    </style>
                                    <div class="scrollable-table-container">
                                        <table>
                                            <thead>
                                                <tr>
                                                    <th>Task ID</th>
                                                    <th>Task</th>
                                                    <th>Description</th>
                                                    <th>Time</th>
                                                    <th>Status</th>
                                                    <th>Priority</th>
                                                    <th>Due Date</th>
                                                    <th>Completed Date</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                    """
                                    for row in data:
                                        html_table += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td><td>{row[5]}</td><td>{row[6]}</td><td>{row[7]}</td></tr>"
                                    html_table += "</tbody></table></div>"
                                    st.markdown(html_table, unsafe_allow_html=True)

                            
                            with tab3:
                                with st.form(key="TMupdate", clear_on_submit=True):
                                    st.subheader("Update an existing Task of yours!")
                                    TM_ID1 = st.text_input("Enter Your Task ID to Update:")  # Assuming this is the ID or unique identifier

                                    # Define input fields for update
                                    TM_Task1 = st.text_input("Enter new Task (optional):")
                                    TM_Desc1 = st.text_area("Enter new Task Description (optional): ")
                                    TM_Time1 = st.time_input("Enter new Time (optional):")
                                    TM_Status1 = st.text_input("Enter new Task Status (optional):")
                                    TM_Priority1 = st.selectbox("Select New Priority (optional):", ["High", "Medium", "Low"])
                                    TM_DueDate1 = st.date_input("Enter new Due Date (optional):")
                                    TM_CompletionDate1 = st.date_input("Enter new Completion Date (optional):")
                                    submit = st.form_submit_button("Update")

                                if submit:
                                    if not TM_ID1:
                                        st.error("Task ID is required to update the record.")
                                    else:
                                        # Construct the SQL update query based on provided inputs
                                        update_fields = []

                                        if TM_Task1:
                                            update_fields.append(f"task = '{TM_Task1}'")
                                        if TM_Desc1:
                                            update_fields.append(f"description = '{TM_Desc1}'")
                                        if TM_Time1:
                                            update_fields.append(f"time = '{TM_Time1.strftime('%H:%M:%S')}'")  # Convert time to string
                                        if TM_Status1:
                                            update_fields.append(f"status = '{TM_Status1}'")
                                        if TM_Priority1:
                                            update_fields.append(f"priority = '{TM_Priority1}'")  # Use quotes
                                        if TM_DueDate1:
                                            update_fields.append(f"due_date = '{TM_DueDate1}'")  # Use quotes
                                        if TM_CompletionDate1:
                                            update_fields.append(f"completed_date = '{TM_CompletionDate1}'")  # Use quotes

                                        if update_fields:
                                            # Join all the update fields into a single string
                                            update_query = ", ".join(update_fields)
                                            sql = f"UPDATE TM SET {update_query} WHERE task_id = {TM_ID1}"  # Use appropriate identifier for WHERE clause

                                            try:
                                                mycursor.execute(sql)
                                                mydb.commit()
                                                st.success("Task updated successfully!")
                                                st.session_state.active_tab = "Display"  # Switch to the Display tab after update
                                            except Exception as e:
                                                st.error(f"Failed to update task: {e}")
                                        else:
                                            st.warning("No updates were made because no fields were provided.")

                            
                            with tab4:
                                with st.form(key="TMdelete_record", clear_on_submit=True):
                                    st.session_state.delrec = True
                                    if st.session_state.delrec: 
                                        st.subheader("Delete a Task!")
                                        task_id = st.text_input("Enter Task ID to delete:")
                                        submit = st.form_submit_button("Delete Record")

                                    if submit:
                                        if not task_id:
                                            st.warning("Please enter a Task ID.")
                                        else:
                                            sql = "DELETE FROM TM WHERE Task_id = %s"  # Use %s for parameterized query
                                            try:
                                                # Execute the delete operation
                                                mycursor.execute(sql, (task_id,))  # Pass task_id as a tuple
                                                mydb.commit()

                                                # Check how many rows were affected (deleted)
                                                if mycursor.rowcount > 0:
                                                    st.success("Record Deleted!")
                                                else:
                                                    st.warning("No record found with that Task ID.")

                                            except Exception as e:
                                                st.error(f"Failed to delete record: {e}")



                if task == "Patient":
                        st.session_state.patient = True
                        st.session_state.userdisplay = False

                        if st.session_state.patient: 
                            st.markdown(
                            """
                            <style>
                            div.streamlit-expanderHeader {
                            margin-bottom: 10px;
                            }
                            div[data-baseweb="tab-list"] button {
                            margin-right: 100px;  /* Adjust the spacing between tabs */
                            padding: 10px 20px;  /* Adjust the padding inside each tab */
                            font-size: 100px;     /* Adjust the font size */
                            }
                            </style>
                            """,
                            unsafe_allow_html=True
                            )
                        tab1 , tab2, tab3, tab4 = st.tabs(["Create", "Display", "Update", "Delete"])

                        # Create Record
                        with tab1:
                            with st.form(key="patientcreate_form", clear_on_submit=True):
                                st.subheader("Create or insert a record!")
                                patient_id = st.text_input("Enter patient's ID:")
                                patient_name = st.text_input("Enter patient's name:")
                                patient_sex = st.selectbox("Select gender:", ["Select","Male", "Female"])
                                patient_age = st.text_input("Enter age:", key="patient_age")
                                patient_dob = st.text_input("Enter patient's date of birth:")
                                patient_wno = st.text_input("Enter patient's Ward Number:")
                                patient_problem = st.text_input("Enter patient's symptoms and problem:")
                                patient_joiningdate = st.text_input("Enter patient's date of joining:")
                                patient_leavingdate = st.text_input("Enter patient's date of leaving:")
                                submit = st.form_submit_button("Create/Add Record")

                            if submit:
                                sql = "INSERT INTO _info (patient_id, patient_name, patient_sex, patient_age, patient_dob, patient_wno, patient_problem, patient_joiningdate, patient_leavingdate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                values = (patient_id, patient_name, patient_sex, patient_age, patient_dob, patient_wno, patient_problem, patient_joiningdate, patient_leavingdate)
                                try:
                                    mycursor.execute(sql, values)
                                    mydb.commit()
                                    st.success("Created/Added record.")
                                except Exception as e:
                                    st.error(f"Failed to create record: {e}")

                        # Display Record         
                        with tab2:
                            st.subheader("Records of Chettinad Hospital:")
                            choice = st.selectbox(f"**Select the Display Method:**",["Display" ,"Search"])
                            if choice == "Display":
                                    sql = "SELECT * FROM patient_info"
                                    mycursor.execute(sql)
                                    data = mycursor.fetchall()

                                    if len(data) == 0:
                                        st.write("No records found.")
                                    else:
                                        html_table = """
                                        <style>
                                            .scrollable-table-container {
                                                max-height: 600px;
                                                overflow-y: auto;
                                            }
                                            table {
                                                width: 100%;  /* Smaller table width */
                                                border-collapse: collapse;
                                                margin: 25px auto;  /* Center the table */
                                                font-size: 14px;  /* Medium font size */
                                                text-align: left;
                                            }
                                            th, td {
                                                padding: 10px 12px;  /* Adjust padding */
                                            }
                                            th {
                                                background-color: #333;
                                                color: #ffffff;
                                            }
                                            tr:nth-child(even) {
                                                background-color: #777;
                                            }
                                            tr:nth-child(odd) {
                                                background-color: #555;
                                            }
                                        </style>
                                        <div class="scrollable-table-container">
                                            <table>
                                                <thead>
                                                    <tr>
                                                        <th>ID</th>
                                                        <th>Name</th>
                                                        <th>Gender</th>
                                                        <th>Age</th>
                                                        <th>DOB</th>
                                                        <th>Ward No.</th>
                                                        <th>Symptoms and Problems</th>
                                                        <th>Date of joining</th>
                                                        <th>Date of leaving</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                        """
                                        for row in data:
                                            html_table += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td><td>{row[5]}</td><td>{row[6]}</td><td>{row[7]}</td><td>{row[8]}</td></tr>"
                                        html_table += "</tbody></table></div>"
                                        st.markdown(html_table, unsafe_allow_html=True)

                            if choice == "Search":
                                st.session_state.showbox = True
                                st.session_state.showtable = False

                                if st.session_state.showbox:
                                    with st.form(key="Docdisplay_form", clear_on_submit=True): 
                                        st.subheader("Search an existing record!")  
                                        patient_id = st.text_input("Enter patient's ID (optional):")  
                                        patient_name = st.text_input("Enter patient's name (optional):")  
                                        patient_problem = st.text_input("Enter Symptoms and Problems (optional):")  
                                        patient_joiningdate = st.text_input("Enter patient's date of joining (optional):")  
                                        submit = st.form_submit_button("Search") 

                                    if submit:
                                        st.session_state.showtable = True
                                        st.session_state.showbox = False

                                        if st.session_state.showtable and not st.session_state.showbox:
                                            search_fields = []  
                                            
                                            if patient_id:  
                                                search_fields.append(f"patient_id = '{patient_id}'")
                                            if patient_name:  
                                                search_fields.append(f"patient_name LIKE '%{patient_name}%'")
                                            if patient_problem:  
                                                search_fields.append(f"patient_problem LIKE '%{patient_problem}%'")
                                            if patient_joiningdate:  
                                                # Convert date object to string in 'YYYY-MM-DD' format
                                                formatted_date = patient_joiningdate.strftime('%Y-%m-%d')
                                                search_fields.append(f"patient_joiningdate = '{formatted_date}'")
                                                                
                                            # Check if there are search fields
                                            if search_fields:  
                                                search_query = " AND ".join(search_fields)  
                                                sql = f"SELECT * FROM patient_info WHERE {search_query}"    
                                                mycursor.execute(sql)  
                                                data = mycursor.fetchall()  
                                                header = ["ID", "Name", "Sex", "Age", "DOB", "Ward No.", "Symptoms and Problems", "Date of Joining", "Date of Leaving"]

                                                if len(data) == 0:  
                                                    st.write("No records found.")  
                                                else:   
                                                    df = pd.DataFrame(data, columns=header)
                                                    st.table(df)
                                            else:
                                                st.write("Please enter at least one search criterion.")


                        # Delete Record      
                        with tab4:
                            with st.form(key="patientdelete_record", clear_on_submit=True):
                                st.session_state.delrec = True
                                if st.session_state.delrec: 
                                    st.subheader("Delete a record!")
                                    doctor_id = st.text_input("Enter patient's ID to delete:")
                                    submit = st.form_submit_button("Delete Record")

                                if submit:
                                    sql = "DELETE FROM patient_info WHERE patient_id = {}".format(doctor_id)
                                    try:
                                        mycursor.execute(sql)
                                        mydb.commit()

                                        # Check if the table is now empty
                                        mycursor.execute("SELECT * FROM patient")
                                        data = mycursor.fetchall()
                                        if len(data) == 0:
                                            st.write("No records found.")
                                        else:
                                            st.success("Record Deleted!")


                                    except Exception as e:
                                        st.error(f"Failed to delete record: {e}")

                            with tab3:
                                with st.form(key= "patientupdate", clear_on_submit=True):
                                    st.subheader("Update an existing record!")
                                    doctor_id = st.text_input("Enter Patient's ID:", key="doctor_id_update")

                                    # Define input fields for update
                                    patient_name = st.text_input("Enter new patient's name (optional):")
                                    patient_sex = st.selectbox("Select new patient (optional):", ["Select", "Male", "Female"])
                                    patient_age = st.text_input("Enter new age (optional):")
                                    patient_dob = st.text_input("Enter new patient's date of birth (optional):")
                                    patient_wno = st.text_input("Enter new patient's ward no. (optional):")
                                    patient_dateofjoining = st.text_input("Enter new patient's joining (optional):")
                                    patient_dateofleaving = st.text_input("Enter new patient's date of leaving (optional):")
                                    patient_problem = st.text_input("Enter new patient's problem (optional):")
                                    submit = st.form_submit_button("Update")


                                if submit:
                                    if not doctor_id:
                                        st.error("Patient ID is required to update the record.")
                                    else:
                                        # Construct the SQL update query based on provided inputs
                                        update_fields = []

                                        if patient_name:
                                            update_fields.append(f"patient_name = '{patient_name}'")
                                        if patient_sex != "Select":
                                            update_fields.append(f"patient_sex = '{patient_sex}'")
                                        if patient_age:
                                            update_fields.append(f"patient_age = {patient_age}")
                                        if patient_dob:
                                            update_fields.append(f"patient_dob = '{patient_dob}'")
                                        if patient_wno:
                                            update_fields.append(f"patient_wno = {patient_wno}")
                                        if patient_dateofjoining:
                                            update_fields.append(f"patient_joiningdate = {patient_dateofjoining}")
                                        if patient_dateofleaving:
                                            update_fields.append(f"patient_leavingdate  = '{patient_dateofleaving}'")
                                        if patient_problem: 
                                            update_fields.append(f"patient_problem = '{patient_problem}'")

                                        if update_fields:
                                            # Join all the update fields into a single string
                                            update_query = ", ".join(update_fields)
                                            sql = f"UPDATE patient_info SET {update_query} WHERE patient_id = {doctor_id}"

                                            try:
                                                mycursor.execute(sql)
                                                mydb.commit()
                                                st.success("Record updated successfully!")
                                                st.session_state.active_tab = "Display"  # Switch to the Display tab after update
                                            except Exception as e:
                                                st.error(f"Failed to update record: {e}")
                                        else:
                                            st.warning("No updates were made because no fields were provided.")

    else:
            st.header(f"Welcome, {st.session_state.username if 'username' in st.session_state else 'Doctor'}")
            st.markdown("Click the buttons below to execute a function!")
            st.session_state.user_type = "Select"

            # Create a two-column layout for "Previous" and "Signout" buttons
            col1, _, col2 = st.columns([1, 5, 1])  # The middle column is much wider to create space between the buttons
        
        
            with col2:
                signout_button = st.button('Signout', key="signout_button")
                if signout_button:
                    st.session_state.signedout = True
                    st.session_state.username = ''
                    st.session_state.user_type = "Select"
                    st.session_state.doctorsignedout = True
                    st.rerun()

            # Show options only if a user type is selected
            if st.session_state.user_type == "Select":
                selected_option = st.selectbox("Select Table", ["Doctor" ,"Patient"], key="user_type_selector")
                if selected_option != "Select":
                    st.session_state.user_type = selected_option
                if "user_type_selector " not in st.session_state:
                    selected_option = st.selectbox
            

            if st.session_state.user_type == 'Doctor': 

                st.markdown(
                    """
                    <style>
                    div.streamlit-expanderHeader {
                    margin-bottom: 10px;
                    }
                    div[data-baseweb="tab-list"] button {
                        margin-right: 100px;  /* Adjust the spacing between tabs */
                        padding: 10px 20px;  /* Adjust the padding inside each tab */
                        font-size: 100px;     /* Adjust the font size */
                    }
                    </style>
                    """,
                    unsafe_allow_html=True
                )
                tab1 , tab2, tab3, tab4 = st.tabs(["Create", "Display", "Update", "Delete"])

                # Create Record
                with tab1:
                    with st.form(key="create_form", clear_on_submit=True):
                        st.subheader("Create or insert a record!")
                        doctor_id = st.text_input("Enter doctor's ID:")
                        doctor_name = st.text_input("Enter doctor's name:")
                        doctor_sex = st.selectbox("Select gender:", ["Select","Male", "Female"])
                        doctor_age = st.text_input("Enter age:")
                        doctor_dept = st.text_input("Enter doctor's department:")
                        doctor_exp = st.text_input("Enter doctor's experience in years:")
                        doctor_salary = st.text_input("Enter doctor's salary:")
                        doctor_date_of_joining = st.text_input("Enter doctor's date of joining:")
                        submit = st.form_submit_button("Create/add record")
                    
                    if submit:
                        sql = "INSERT INTO doctor_info VALUES({}, '{}', '{}', '{}', {}, {}, '{}', '{}')".format(doctor_id, doctor_name, doctor_age, doctor_dept, doctor_exp, doctor_salary, doctor_date_of_joining, doctor_sex)
                        try:
                            mycursor.execute(sql)
                            mydb.commit()
                            st.success("Record created/added!")
                        except Exception as e:
                            st.error(f"Failed to create record: {e}")

                # Display Record         
                with tab2:
                    st.subheader("Records of Chettinad Hospital:")
                    choice = st.selectbox(f"**Select the Display Method:**",["Display" ,"Search"])
                    if choice == "Display":
                            sql = "SELECT * FROM doctor_info"
                            mycursor.execute(sql)
                            data = mycursor.fetchall()

                            if len(data) == 0:
                                st.write("No records found.")
                            else:
                                html_table = """
                                <style>
                                    .scrollable-table-container {
                                        max-height: 600px;
                                        overflow-y: auto;
                                    }
                                    table {
                                        width: 100%;  /* Smaller table width */
                                        border-collapse: collapse;
                                        margin: 25px auto;  /* Center the table */
                                        font-size: 14px;  /* Medium font size */
                                        text-align: left;
                                    }
                                    th, td {
                                        padding: 10px 12px;  /* Adjust padding */
                                    }
                                    th {
                                        background-color: #333;
                                        color: #ffffff;
                                    }
                                    tr:nth-child(even) {
                                        background-color: #777;
                                    }
                                    tr:nth-child(odd) {
                                        background-color: #555;
                                    }
                                </style>
                                <div class="scrollable-table-container">
                                    <table>
                                        <thead>
                                            <tr>
                                                <th>ID</th>
                                                <th>Name</th>
                                                <th>Gender</th>
                                                <th>Age</th>
                                                <th>Department</th>
                                                <th>Experience</th>
                                                <th>Salary</th>
                                                <th>Date of Joining</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                """
                                for row in data:
                                    html_table += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td><td>{row[5]}</td><td>{row[6]}</td><td>{row[7]}</td></tr>"
                                html_table += "</tbody></table></div>"
                                st.markdown(html_table, unsafe_allow_html=True)

                    if choice == "Search":
                        st.session_state.showbox = True
                        st.session_state.showtable = False
                        
                        
                        if st.session_state.showbox:
                            with st.form(key="Docdisplay_form", clear_on_submit=True): 
                                
                                st.subheader("Search an existing record!")  
                                doctor_id = st.text_input("Enter doctor's ID (optional):")  
                                doctor_name = st.text_input("Enter doctor's name (optional):")  
                                doctor_dept = st.text_input("Enter doctor's department (optional):")  
                                doctor_dateofjoining = st.text_input("Enter doctor's date of joining (optional):")  
                                submit = st.form_submit_button("Search") 
                            
                            if submit:
                                    st.session_state.showtable = True
                                    st.session_state.showbox = False
                                    
                                    if st.session_state.showtable and not st.session_state.showbox:
                                        search_fields = []  
                                        if doctor_id:  
                                            search_fields.append(f"doctor_id = {doctor_id}")  
                                        if doctor_name:  
                                            search_fields.append(f"doctor_name LIKE '%{doctor_name}%'")  
                                        if doctor_dept:  
                                            search_fields.append(f"doctor_dept = '{doctor_dept}'")  
                                        if doctor_dateofjoining:
                                            try:
                                                parsed_date = pd.to_datetime(doctor_dateofjoining).strftime('%Y-%m-%d')
                                                search_fields.append(f"doctor_dateofjoining = '{parsed_date}'")
                                            except Exception:
                                                st.write("Please enter the date in YYYY-MM-DD format.")
                                    
                                        if search_fields:  
                                            search_query = " AND ".join(search_fields)  
                                            sql = f"SELECT * FROM doctor_info WHERE {search_query}"    
                                            mycursor.execute(sql)  
                                            data = mycursor.fetchall()  
                                            header = ["ID",	"Name",	"Gender", "Age", "Department",	"Experience", "Salary",	"Date of Joining"]
                                            if len(data) == 0:  
                                                st.write("No records found.")  
                                            else:   
                                                df = pd.DataFrame(data, columns=header)
                                                st.table(df)
                                        
                                        else:
                                            st.write("Please enter at least one search criterion.")

                # Delete Record      
                with tab4:
                    with st.form(key="delete_record", clear_on_submit=True): 
                            st.subheader("Delete a record!")
                            doctor_id = st.text_input("Enter doctor's ID to delete:")
                            submit = st.form_submit_button("Delete Record")

                    if submit:
                        sql = "DELETE FROM doctor_info WHERE doctor_id = {}".format(doctor_id)
                        try:
                            mycursor.execute("SELECT * FROM doctor_info")
                            data = mycursor.fetchall()
                            if len(data) == 0:
                                st.write("No records found.")
                            else:
                                st.success("Record Deleted!")
                            mycursor.execute(sql)
                            mydb.commit()
                            

                        except Exception as e:
                            st.error(f"Failed to delete record: {e}")

                    with tab3:
                        with st.form(key="Docupdate_form", clear_on_submit=True):
                            st.subheader("Update an existing record!")
                            doctor_id = st.text_input("Enter doctor's ID:", key="doctor_id_update")
                            
                            # Define input fields for update
                            doctor_name = st.text_input("Enter new doctor's name (optional):", key="doctor_name_update")
                            doctor_sex = st.selectbox("Select new gender (optional):", ["Select", "Male", "Female"], key="doctor_sex_update")
                            doctor_age = st.text_input("Enter new age (optional):", key="doctor_age_update")
                            doctor_dept = st.text_input("Enter new doctor's department (optional):", key="doctor_dept_update")
                            doctor_exp = st.text_input("Enter new doctor's experience in years (optional):", key="doctor_exp_update")
                            doctor_salary = st.text_input("Enter new doctor's salary (optional):", key="doctor_salary_update")
                            doctor_dateofjoining = st.text_input("Enter new doctor's date of joining (optional):", key="doctor_dateofjoining_update")
                            submit = st.form_submit_button("Update")


                        if submit:
                            if not doctor_id:
                                st.error("Doctor ID is required to update the record.")
                            else:
                                # Construct the SQL update query based on provided inputs
                                update_fields = []

                                if doctor_name:
                                    update_fields.append(f"name = '{doctor_name}'")
                                if doctor_sex != "Select":
                                    update_fields.append(f"gender = '{doctor_sex}'")
                                if doctor_age:
                                    update_fields.append(f"age = {doctor_age}")
                                if doctor_dept:
                                    update_fields.append(f"dept = '{doctor_dept}'")
                                if doctor_exp:
                                    update_fields.append(f"exp = {doctor_exp}")
                                if doctor_salary:
                                    update_fields.append(f"salary = {doctor_salary}")
                                if doctor_dateofjoining:
                                    update_fields.append(f"dateofjoining = '{doctor_dateofjoining}'")

                                if update_fields:
                                    # Join all the update fields into a single string
                                    update_query = ", ".join(update_fields)
                                    sql = f"UPDATE doctor_info SET {update_query} WHERE doctor_id = {doctor_id}"
                                
                                    try:
                                        mycursor.execute(sql)
                                        mydb.commit()
                                        st.success("Record updated successfully!")
                                    except Exception as e:
                                        st.error(f"Failed to update record: {e}")
                                else:
                                    st.warning("No updates were made because no fields were provided.")
    
            elif st.session_state.user_type == 'Patient':
                st.markdown(
                    """
                    <style>
                    div.streamlit-expanderHeader {
                      margin-bottom: 10px;
                    }
                    div[data-baseweb="tab-list"] button {
                      margin-right: 100px;  /* Adjust the spacing between tabs */
                      padding: 10px 20px;  /* Adjust the padding inside each tab */
                      font-size: 100px;     /* Adjust the font size */
                    }
                    </style>
                    """,
                    unsafe_allow_html=True
                )
                tab1 , tab2, tab3, tab4 = st.tabs(["Create", "Display", "Update", "Delete"])

                # Create Record
                with tab1:
                    with st.form(key="patientcreate_form", clear_on_submit=True):
                        st.subheader("Create or insert a record!")
                        patient_id = st.text_input("Enter patient's ID:")
                        patient_name = st.text_input("Enter patient's name:")
                        patient_sex = st.selectbox("Select gender:", ["Select","Male", "Female"])
                        patient_age = st.text_input("Enter age:", key="patient_age")
                        patient_dob = st.text_input("Enter patient's date of birth:")
                        patient_wno = st.text_input("Enter patient's Ward Number:")
                        patient_problem = st.text_input("Enter patient's symptoms and problem:")
                        patient_joiningdate = st.text_input("Enter patient's date of joining:")
                        patient_leavingdate = st.text_input("Enter patient's date of leaving:")
                        submit = st.form_submit_button("Create/Add Record")

                    if submit:
                        sql = "INSERT INTO patient_info (patient_id, patient_name, patient_sex, patient_age, patient_dob, patient_wno, patient_problem, patient_joiningdate, patient_leavingdate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        values = (patient_id, patient_name, patient_sex, patient_age, patient_dob, patient_wno, patient_problem, patient_joiningdate, patient_leavingdate)
                        try:
                            mycursor.execute(sql, values)
                            mydb.commit()
                            st.success("Created/Added record.")
                        except Exception as e:
                            st.error(f"Failed to create record: {e}")

                # Display Record         
                with tab2:
                    st.subheader("Records of Chettinad Hospital:")
                    choice = st.selectbox(f"**Select the Display Method:**",["Display" ,"Search"])
                    if choice == "Display":
                            sql = "SELECT * FROM patient_info"
                            mycursor.execute(sql)
                            data = mycursor.fetchall()

                            if len(data) == 0:
                                st.write("No records found.")
                            else:
                                html_table = """
                                <style>
                                    .scrollable-table-container {
                                        max-height: 600px;
                                        overflow-y: auto;
                                    }
                                    table {
                                        width: 100%;  /* Smaller table width */
                                        border-collapse: collapse;
                                        margin: 25px auto;  /* Center the table */
                                        font-size: 14px;  /* Medium font size */
                                        text-align: left;
                                    }
                                    th, td {
                                        padding: 10px 12px;  /* Adjust padding */
                                    }
                                    th {
                                        background-color: #333;
                                        color: #ffffff;
                                    }
                                    tr:nth-child(even) {
                                        background-color: #777;
                                    }
                                    tr:nth-child(odd) {
                                        background-color: #555;
                                    }
                                </style>
                                <div class="scrollable-table-container">
                                    <table>
                                        <thead>
                                            <tr>
                                                <th>ID</th>
                                                <th>Name</th>
                                                <th>Gender</th>
                                                <th>Age</th>
                                                <th>DOB</th>
                                                <th>Ward No.</th>
                                                <th>Symptoms and Problems</th>
                                                <th>Date of joining</th>
                                                <th>Date of leaving</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                """
                                for row in data:
                                    html_table += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td><td>{row[5]}</td><td>{row[6]}</td><td>{row[7]}</td><td>{row[8]}</td></tr>"
                                html_table += "</tbody></table></div>"
                                st.markdown(html_table, unsafe_allow_html=True)

                    if choice == "Search":
                        st.session_state.showbox = True
                        st.session_state.showtable = False

                        if st.session_state.showbox:
                            with st.form(key="Docdisplay_form", clear_on_submit=True): 
                                st.subheader("Search an existing record!")  
                                patient_id = st.text_input("Enter patient's ID (optional):")  
                                patient_name = st.text_input("Enter patient's name (optional):")  
                                patient_problem = st.text_input("Enter Symptoms and Problems (optional):")  
                                patient_joiningdate = st.text_input("Enter patient's date of joining (optional):")  
                                submit = st.form_submit_button("Search") 

                            if submit:
                                st.session_state.showtable = True
                                st.session_state.showbox = False

                                if st.session_state.showtable and not st.session_state.showbox:
                                    search_fields = []  
                                    
                                    if patient_id:  
                                        search_fields.append(f"patient_id = '{patient_id}'")
                                    if patient_name:  
                                        search_fields.append(f"patient_name LIKE '%{patient_name}%'")
                                    if patient_problem:  
                                        search_fields.append(f"patient_problem LIKE '%{patient_problem}%'")
                                    if patient_joiningdate:  
                                        # Convert date object to string in 'YYYY-MM-DD' format
                                        formatted_date = patient_joiningdate.strftime('%Y-%m-%d')
                                        search_fields.append(f"patient_joiningdate = '{formatted_date}'")
                                                        
                                    # Check if there are search fields
                                    if search_fields:  
                                        search_query = " AND ".join(search_fields)  
                                        sql = f"SELECT * FROM patient_info WHERE {search_query}"    
                                        mycursor.execute(sql)  
                                        data = mycursor.fetchall()  
                                        header = ["ID", "Name", "Sex", "Age", "DOB", "Ward No.", "Symptoms and Problems", "Date of Joining", "Date of Leaving"]

                                        if len(data) == 0:  
                                            st.write("No records found.")  
                                        else:   
                                            df = pd.DataFrame(data, columns=header)
                                            st.table(df)
                                    else:
                                        st.write("Please enter at least one search criterion.")


                # Delete Record      
                with tab4:
                    with st.form(key="patientdelete_record", clear_on_submit=True):
                        st.session_state.delrec = True
                        if st.session_state.delrec: 
                            st.subheader("Delete a record!")
                            patient_id = st.text_input("Enter patient's ID to delete:")
                            submit = st.form_submit_button("Delete Record")

                        if submit:
                            if not patient_id:
                                st.warning("Please enter a valid patient ID.")
                            else:
                                mycursor.execute("SELECT * FROM patient_info")
                                data = mycursor.fetchall()
                                # Use parameterized query to avoid SQL injection
                                sql = "DELETE FROM patient_info WHERE patient_id = %s"
                                try:
                                    mycursor.execute(sql, (patient_id,))  # Pass patient_id as a tuple
                                    mydb.commit()

                                    # Check if the record was successfully deleted
                                    if mycursor.rowcount == 0:
                                        st.warning("No record found with the given patient ID.")
                                    else:
                                        # Check if the table still contains records
                                        if len(data) == 0:
                                            st.write("No records found.")
                                        else:
                                            st.success("Record Deleted!")

                                except Exception as e:
                                    st.error(f"Failed to delete record: {e}")


                    with tab3:
                        with st.form(key= "patientupdate", clear_on_submit=True):
                            st.subheader("Update an existing record!")
                            doctor_id = st.text_input("Enter Patient's ID:", key="doctor_id_update")

                            # Define input fields for update
                            patient_name = st.text_input("Enter new patient's name (optional):")
                            patient_sex = st.selectbox("Select new patient (optional):", ["Select", "Male", "Female"])
                            patient_age = st.text_input("Enter new age (optional):")
                            patient_dob = st.text_input("Enter new patient's date of birth (optional):")
                            patient_wno = st.text_input("Enter new patient's ward no. (optional):")
                            patient_dateofjoining = st.text_input("Enter new patient's joining (optional):")
                            patient_dateofleaving = st.text_input("Enter new patient's date of leaving (optional):")
                            patient_problem = st.text_input("Enter new patient's problem (optional):")
                            submit = st.form_submit_button("Update")


                        if submit:
                            if not doctor_id:
                                st.error("Patient ID is required to update the record.")
                            else:
                                # Construct the SQL update query based on provided inputs
                                update_fields = []

                                if patient_name:
                                    update_fields.append(f"patient_name = '{patient_name}'")
                                if patient_sex != "Select":
                                    update_fields.append(f"patient_sex = '{patient_sex}'")
                                if patient_age:
                                    update_fields.append(f"patient_age = {patient_age}")
                                if patient_dob:
                                    update_fields.append(f"patient_dob = '{patient_dob}'")
                                if patient_wno:
                                    update_fields.append(f"patient_wno = {patient_wno}")
                                if patient_dateofjoining:
                                    update_fields.append(f"patient_joiningdate = {patient_dateofjoining}")
                                if patient_dateofleaving:
                                    update_fields.append(f"patient_leavingdate  = '{patient_dateofleaving}'")
                                if patient_problem: 
                                    update_fields.append(f"patient_problem = '{patient_problem}'")

                                if update_fields:
                                    # Join all the update fields into a single string
                                    update_query = ", ".join(update_fields)
                                    sql = f"UPDATE patient_info SET {update_query} WHERE patient_id = {doctor_id}"

                                    try:
                                        mycursor.execute(sql)
                                        mydb.commit()
                                        st.success("Record updated successfully!")
                                        st.session_state.active_tab = "Display"  # Switch to the Display tab after update
                                    except Exception as e:
                                        st.error(f"Failed to update record: {e}")
                                else:
                                    st.warning("No updates were made because no fields were provided.")
            
                

if __name__ == "__main__":
    main()
