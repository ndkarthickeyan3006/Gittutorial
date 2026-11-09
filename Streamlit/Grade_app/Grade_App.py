
import streamlit as st
import pandas as pd

# 1. Page configuration
st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Grade Manager")
st.write("Add students and view their grades.")

# 2. Grade calculation
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

# 3. Initialize session state
if "students" not in st.session_state:
    st.session_state.students = []

# 4. Form to add students
st.subheader("Add a student")

with st.form("add_student_form", clear_on_submit=True):
    name = st.text_input("Student name")

    mark = st.number_input(
        "Student mark",
        min_value=0,
        max_value=100,
        value=0,
        step=1
    )

    submitted = st.form_submit_button("Add student")

    if submitted:
        if not name.strip():
            st.error("Please enter a student name.")
        else:
            student = {
                "Name": name.strip(),
                "Mark": int(mark),
                "Grade": get_grade(int(mark))
            }

            st.session_state.students.append(student)
            st.success(f"{name.strip()} added successfully!")

# 5. Display results
st.subheader("Student results")

if st.session_state.students:

    results_df = pd.DataFrame(st.session_state.students)

    st.dataframe(
        results_df,
        use_container_width=True,
        hide_index=True
    )

    marks = results_df["Mark"]

    average = marks.mean()
    highest = marks.max()
    lowest = marks.min()

    # 6. Class metrics
    st.subheader("Class statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Class Average", f"{average:.2f}")
    col2.metric("Highest Mark", int(highest))
    col3.metric("Lowest Mark", int(lowest))

    # Optional clear button
    if st.button("Clear all students"):
        st.session_state.students = []
        st.rerun()

else:
    st.info("No students added yet.")
