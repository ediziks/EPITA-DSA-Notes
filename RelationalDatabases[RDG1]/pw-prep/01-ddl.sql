create table contacts
(
	contact_email varchar(255) not null
		constraint contacts_pk
			primary key,
	contact_first_name varchar(255),
	contact_last_name varchar(500),
	contact_address varchar(700),
	contact_city varchar(255),
	contact_country varchar(255),
	contact_birthdate date
);

comment on table contacts is 'contains informations about contacts';



create table populations
(
	population_code varchar(10) not null,
	population_year integer not null,
	population_period varchar(10) not null,
	constraint populations_pk
		primary key (population_code, population_year, population_period)
);

comment on table populations is 'Different populations over time';

create table students
(
	student_epita_email varchar(255) not null
		constraint students_pk
			primary key,
	student_contact_ref varchar(255) not null
		constraint students_contacts_fk
			references contacts,
	student_enrollment_status varchar(50) not null,
	student_population_period_ref varchar(10) not null,
	student_population_year_ref integer not null,
	student_population_code_ref varchar(5) not null
);



create table teachers
(
	teacher_contact_ref text,
	teacher_epita_email text not null
		constraint teachers_pk
			primary key,
	teacher_study_level integer
);



create table courses
(
	course_code text not null,
	course_rev integer not null,
	duration integer,
	course_last_rev integer,
	course_name text,
	course_description text,
	constraint courses_pk
		primary key (course_code, course_rev)
);



create table exams
(
	exam_course_code text not null,
	exam_course_rev integer not null,
	exam_weight integer,
	exam_type text not null,
	constraint exams_pk
		primary key (exam_course_code, exam_course_rev, exam_type)
);


create table sessions
(
	session_course_ref text not null,
	session_course_rev_ref integer not null,
	session_prof_ref text,
	session_date date not null,
	session_start_time text not null,
	session_end_time text not null,
	session_type text,
	session_population_year integer,
	session_population_period text,
	session_room text,
	constraint sessions_pk
		primary key (session_course_ref, session_date, session_start_time, session_end_time)
);



create table attendance
(
	attendance_student_ref text,
	attendance_population_year_ref integer,
	attendance_course_ref text,
	attendance_course_rev integer,
	attendance_session_date_ref text,
	attendance_session_start_time text,
	attendance_session_end_time text,
	attendance_presence integer
);


create table programs
(
	program_course_code_ref text not null,
	program_course_rev_ref integer not null,
	program_assignment text not null,
	constraint programs_pk
		primary key (program_course_code_ref, program_course_rev_ref, program_assignment),
	constraint programs_courses_course_code_course_rev_fk
		foreign key (program_course_code_ref, program_course_rev_ref) references courses
);


create table grades
(
	grade_student_epita_email_ref text not null
		constraint grades_students_student_epita_email_fk
			references students,
	grade_course_code_ref text not null,
	grade_course_rev_ref integer not null,
	grade_exam_type_ref text not null,
	grade_score integer,
	constraint grades_pk
		primary key (grade_student_epita_email_ref, grade_course_rev_ref, grade_course_code_ref, grade_exam_type_ref)
);

