#!pip3 install ipywidgets-toggle-buttons

from IPython.core.magic import register_line_magic
import clingo
from clingo.control import Control

from IPython.display import display
import ipywidgets as widgets
from ipywidgets_toggle_buttons import MultiToggleButtons
import pandas as pd
import numpy as np
import os
import re

# create new empty files for:

# user input
#open('files/user_course.lp', 'w').close()

# clingo output
#open('output/clingo_output.txt', 'w').close()

# clingo validation
#open('output/validate_output.txt', 'w').close()

class main:
    def __init__(self):

        # initiate semester with 0
        self.sem = 0

        # get module list for checkbox values
        with open("files/module_index.txt") as file:
            self.modules = [line.rstrip() for line in file]

        # get full course names
        with open("files/course_names.txt") as file:
            #course_names = [[line.rstrip()] for line in file]
            self.course_names = pd.read_csv(file)

        # get image with example study schedule
        with open("files/studyreg_cogsys.png", "rb") as file:
            image = file.read()

        # set button style
        style = {'description_width': 'initial'}

        # initiate colours for print statements
        RED = '\033[91m'
        END = '\033[0m'
        BOLD = '\033[1m'
        GREEN = '\033[92m'
        UNDERLINE = '\033[4m'

        ##### CREATE WIDGETS #####

        # checkboxes for selecting modules that were already done in previous or current semesters
        self.checkboxes_done = [widgets.Checkbox(value=False, description=label.upper()) for label in self.modules if label != "thesis"]
        self.module_done = widgets.VBox(children=self.checkboxes_done)

        # checkboxes for selecting modules that are wanted for the upcoming semesters
        self.checkboxes_want = [widgets.Checkbox(value=False, description=label.upper()) for label in self.modules]
        self.module_want = widgets.VBox(children=self.checkboxes_want)

        # widget for selection of semesters
        self.semester = widgets.BoundedIntText(
            description='Semesters:',
            min=1,
            max=8
        )

        # widget for selection of current semester
        self.next_sem = widgets.RadioButtons(
            options=['Winter Semester', 'Summer Semester'],
            value='Winter Semester',
            description='The next semester is a ...',
            disabled=False,
            style = style
        )

        # widget for selection of foundation modules
        self.fm_select = MultiToggleButtons(
            options=['Foundations of Linguistics (FM1)',
                    'Foundations of Mathematics (FM2)',
                    'Foundations of Computer Science (FM3)'],
            description='',
            disabled=False,
            max_chosen_values=2,
            button_style=''
        )

        # widget for showing the example study schedule
        self.studyreg = widgets.Image(
                value=image,
                format='png',
                width=500,
                height=700,
        )

        ##### CREATE BUTTONS #####

        # button for saving selection of foundation modules
        self.btn_save_selection = widgets.Button(
            description='Save Selection',
            disabled=False,
            button_style='success'
        )

        # button for clearing input (resets the input)
        self.btn_clear_input = widgets.Button(
            description='Clear User Input',
            disabled=False,
            button_style=''
        )

        # button for validating the input
        self.btn_validate = widgets.Button(
            description='Validate Choice',
            disabled=False,
            button_style='danger'
        )

        # button for showing exemplary study schedule
        self.btn_show_sched = widgets.Button(
                description="Exemplary Schedule",
                layout=style,
                button_style="info",
                tooltip='Show the exemplary study schedule'
        )

        ##### CREATE OUTPUTS #####

        # initiate outputs
        self.input_output = widgets.Output()
        self.valid_output = widgets.Output()
        self.image_output = widgets.Output()

        # style the widgets
        self.ui_done = widgets.VBox([widgets.Label(value='Select modules you already did',style=dict(font_weight='bold')), self.module_done])#, self.btn_save_module_done]) #, self.output])
        self.ui_want = widgets.VBox([widgets.Label(value='Select modules you want to do',style=dict(font_weight='bold')), self.module_want])#, self.btn_save_module_want]) #, self.output])
        self.ui_fms = widgets.VBox([widgets.Label(value='Select foundation modules you need to take', style=dict(font_weight='bold')), self.fm_select, self.btn_save_selection, self.input_output]) #, self.btn_save_fm, self.input_output]) #, self.output])
        self.ui_sem = widgets.VBox([widgets.Label(value='For how many semesters do you want to get a timetable suggestion?',style=dict(font_weight='bold')), self.semester, self.next_sem]) #, self.btn_save_semester])
        self.ui_valid = widgets.HBox([widgets.Label(value='',style=dict(font_weight='bold')), self.btn_validate, self.btn_clear_input])

        # create tab widget for modules done and modules want
        tab_contents = [self.checkboxes_done, self.checkboxes_want]
        children = [self.ui_done, self.ui_want]
        self.tab = widgets.Tab()
        self.tab.children = children
        self.tab.set_title(0, "Modules Finished")
        self.tab.set_title(1, "Module Selection")

        # final interface style
        self.ui = widgets.VBox([widgets.Label(value='Click here to check the exemplary study schedule from the official study regulations:',style=dict(font_weight='bold')), self.btn_show_sched, self.image_output, self.tab, self.ui_sem, self.ui_fms, self.ui_valid, self.valid_output])

        ##### ON CLICK BUTTON FUNCTIONS #####

        # show exemplary schedule
        def show_schedule(bttn):
            with self.image_output:
                display(self.studyreg)

        # save selection into user_course.lp file (= input to clingo)
        def save_selection(bttn):

            # modules finished:
            output_file = open('files/user_course.lp', 'a')
            self.data_done = []
            for i in range(0, len(self.checkboxes_done)): # for each checkbox
                if self.checkboxes_done[i].value == True: # write TRUE values to user_course.lp file
                    self.data_done = self.data_done + [self.checkboxes_done[i].description]
            for i in self.data_done:
                output_file.write('done('+i.lower()+'). ') # we want atoms to look like done(xyz)

            # modules want/ module selection:
            self.data_want = []
            for i in range(0, len(self.checkboxes_want)): # for each checkbox
                if self.checkboxes_want[i].value == True: # write TRUE values to user_course.lp file
                    self.data_want = self.data_want + [self.checkboxes_want[i].description]
            for i in self.data_want:
                output_file.write('want('+i.lower()+'). ') # we want atoms to look like want(xyz)

            # save semester info:
            self.sem = self.semester.value # save chosen semester value
            #output_file = open('user_course.lp', 'a')
            output_file.write('semester('+'1..'+str(self.sem)+'). ') # we want atom to look like semester(1..X)
            if self.next_sem.value == "Winter Semester":
                output_file.write('next_sem(ws). ') # we want atom to look like current_sem(X)
            else:
                output_file.write('next_sem(ss). ')

            # save fms
            self.fm = str(self.fm_select.value) # get value of toggle buttons
            #output_file = open('user_course.lp', 'a')
            if "FM1" in self.fm:
                output_file.write('needed(fm1). ') # we want atom to look like needed(fmX)
            if "FM2" in self.fm:
                output_file.write('needed(fm2). ')
            if "FM3" in self.fm:
                output_file.write('needed(fm3). ')

            # close file
            output_file.close()

            # give information statement of selected values
            with self.input_output:
                print(UNDERLINE+"\nSummary of your selection:\n"+END)

                # information about finished modules
                if self.data_want:
                    print("Finished modules: ", ', '.join(self.data_want)+"\n")
                else:
                    print("You have not finished any modules so far.\n")

                # information about module selection
                if self.data_want:
                    print("Module selection: ", ', '.join(self.data_want)+"\n")
                else:
                    print("No modules selected - Please make a selection and click on 'Save Selection' again.\n")

                # give information about semester selection
                if self.sem != 0:
                    print("Suggestion for ", self.sem, "semester(s)", "\n"
                        "The next semester is a ", self.next_sem.value, "\n")

                if self.fm_select.value:
                    print("Foundation Modules: ", ', '.join(self.fm_select.value),"\n")
                else:
                    print("No foundation modules selected - If that is not correct, please select the foundation modules above.\n")
                print('─' * 60)

        # clear input
        def clear_input(bttn):
            open('files/user_course.lp', 'w').close() # clear user_course.lp file
            open('output/clingo_output.txt', 'w').close() # clear clingo_output.txt file
            open('output/validate_output.txt', 'w').close() # clear validate_output.txt file
            self.input_output.clear_output() # clear input in interface
            self.valid_output.clear_output() # clear error messages from valid button
            with self.valid_output:
                print("*"*45)
                print("Input cleared - Please make another selection") # give feedback to user
                print("*"*45)

        # validate user selection
        def validate(bttn):
            with self.valid_output:
                # clear complete validate output
                self.valid_output.clear_output()
            # access terminal to run clingo, write output to txt file
            os.system('clingo files/user_course.lp files/module_list.lp files/timetable_atoms.lp files/encoding.lp 1 > output/clingo_output.txt') # run encoding
            os.system('clingo files/user_course.lp files/module_list.lp files/validate.lp 1 > output/validate_output.txt') # run validation

            # open clingo output file in readable format
            with open("output/clingo_output.txt", "r") as f:
                self.clingo_out = f.read().replace('\n', ' ')

            # open validate output file in readable format
            with open("output/validate_output.txt", "r") as f:
                self.to_validate = f.read().replace('\n', ' ')

            # if clingo throws an error, give feedback to user
            if "UNSATISFIABLE" in self.clingo_out or "UNKNOWN" in self.clingo_out:
                with self.valid_output:
                    print('*' * 60)
                    print(BOLD+"Oops - your choice is invalid"+END)
                    hard_constraints(self.to_validate) # check hard constraints: what must be changed to make the selection work
                    print(BOLD+"Click on 'Clear User Input' and start again.")
                    print('*' * 60)

            # if information in clingo output is missing, give feedback to user
            elif "sem" not in self.clingo_out:
                with self.valid_output:
                    print('*' * 60)
                    print(BOLD+"Oops - your choice is invalid"+END)
                    hard_constraints(self.to_validate) # check hard constraints: what must be changed to make the selection work
                    print('*' * 60)

            # if clingo does not give an error (= SATISFIABLE)
            else:

                # check soft constraints, i.e. give feedback to user about selection (what is possible or could be improved)
                with self.input_output:
                    print(BOLD+"Please note:\n"+END)
                    soft_constraints(self.to_validate)
                    print(BOLD+GREEN+"\nIf you're happy with your choice, you can proceed."+END)
                    print('─' * 60)

                # if choice is valid
                with self.valid_output:
                    print("\n"+BOLD+GREEN+"YAY - your choice is valid!\n"+END) # give feedback to user

                    # open and clingo output
                    with open("output/clingo_output.txt", "r") as f:
                        self.clingo_out = f.read().replace('\n',' ')

                    try:
                        # if output works, create interface/buttons for showing the timetable
                        output_data = convert_output(self.clingo_out)

                    except:
                        # if not, throw an error message
                        print(RED+"Oops something went wrong - Please click on 'Clear Input' and try again!"+END)

                    # count semesters (get value from semester input)
                    sem_count = []
                    for i in range(self.sem):
                        sem_count.append(i)

                    # create widget for showing the schedule
                    time_dropdown = widgets.Dropdown(
                            options = [i+1 for i in sem_count],
                            value=1,
                            description='Semester',
                            disabled=False)

                    # give output
                    with self.valid_output:

                        # initiate new output widget
                        self.out_time = widgets.Output()

                        ### BUTTONS ###
                        schedule_btn = widgets.Button(description="Show Timetable", button_style="success",layout=style)
                        legend_btn = widgets.Button(description="Show Info", layout=style)
                        clear_btn = widgets.Button(description="Clear Output", layout=style)

                        ### ON CLICK BUTTON FUNCTIONS ###

                        # show timetable for according semester
                        def show_timetable(b):
                            with self.out_time:
                                print("*"*50)

                                # if next semester is a winter/summer semester:
                                if self.next_sem.value == "Winter Semester":
                                    if time_dropdown.value%2!=0:
                                        print("\nSemester "+str(time_dropdown.value)+": Winter")
                                    else:
                                        print("\nSemester "+str(time_dropdown.value)+": Summer")

                                else:
                                    if time_dropdown.value%2!=0:
                                        print("\nSemester "+str(time_dropdown.value)+": Summer")
                                    else:
                                        print("\nSemester "+str(time_dropdown.value)+": Winter")

                                # check if there is a timetable (if we only have online courses, no timetable is available)
                                if timetable_multi(output_data[time_dropdown.value-1])[0].empty == False:
                                    display(timetable_multi(output_data[time_dropdown.value-1])[0]) # show timetable
                                    if timetable_multi(output_data[time_dropdown.value-1])[1]: # if we have online courses, show list of courses
                                        print("Online:", end=" ")
                                        print(*(x for x in timetable_multi(output_data[time_dropdown.value-1])[1]), sep=", ")

                                    else:
                                        pass

                                # if there is no timetable available, only show online courses
                                else:
                                    if timetable_multi(output_data[time_dropdown.value-1])[1]: # if we have online courses, show list of courses
                                        print("Online:", end=" ")
                                        print(*(x for x in timetable_multi(output_data[time_dropdown.value-1])[1]), sep=", ")

                        # give full names of course abbreviations
                        def show_names(b):

                            # get course abbreviations of according semeser (from timetable)
                            data = timetable_multi(output_data[time_dropdown.value-1])[0].to_numpy()
                            short_names = [x for x in ([item for sublist in data for item in sublist]) if x.strip()]

                            try: # get course abbreviations of according semeser (from online courses list)
                                short_names.extend([x for x in timetable_multi(output_data[time_dropdown.value-1])[1]])
                            except: # if no online courses, pass
                                pass

                            with self.out_time:
                                print(UNDERLINE+"\nFull course names for Semester "+str(time_dropdown.value)+END)
                                credits_per_sem = 0
                                for string in set(short_names):

                                    # give full names to according abbreviations
                                    full_name = self.course_names.iat[self.course_names.index[self.course_names["short_name"] == string][0],1]

                                    # retrieve credit count for courses per semester
                                    credits_per_sem += self.course_names.iat[self.course_names.index[self.course_names["short_name"] == string][0],2]
                                    print(string,": ",full_name)

                                # output credits
                                print(BOLD+"\nCREDITS: "+str(credits_per_sem) +END)

                        # to clear output
                        def clear_out(b):
                            self.out_time.clear_output()
                            self.valid_output.clear_output()

                        ### ON CLICK BUTTONS ###
                        schedule_btn.on_click(show_timetable)
                        clear_btn.on_click(clear_out)
                        legend_btn.on_click(show_names)

                        try:
                            # combined widget to show timetable output
                            self.ui_timetable_titles = widgets.HBox([time_dropdown, schedule_btn, legend_btn])
                            self.ui_schedule = widgets.VBox([self.ui_timetable_titles, self.out_time, clear_btn]) #, self.output])

                            # display timetable output widgets when clingo was SATISFIABLE
                            display(self.ui_schedule)

                        except:
                            pass

        ### ON CLICK BUTTON EVENTS ###

        # widget events to save
        self.btn_show_sched.on_click(show_schedule)
        self.btn_save_selection.on_click(save_selection)
        self.btn_clear_input.on_click(clear_input)
        self.btn_validate.on_click(validate)

        ### SHOW TIMETABLE FUNCTIONS ###

        # convert clingo_ouput.txt file to make sure we can put this into a dataframe
        def convert_output(clingo):

            # convert output into nice string
            o = clingo[clingo.find('course('):]
            o = o[:o.find(' SATISFIABLE')]
            o = list(o.split(" "))

            # convert output to nested list format
            o = [el.replace('(', ',') for el in o]
            o = [el.replace(')', '') for el in o]
            o = [char.split(',') for char in o]

            # get list of sem() atoms
            # sem(): give us information about which modules should be taken in which of the semesters
            per_semester = [ x for x in o if "course" not in x ]
            sem_data = pd.DataFrame(per_semester) # convert to dataframe

            # get list of course() atoms
            # course(): give us information about name, day/time for each course
            course_list = [ x for x in o if "sem" not in x ]

            # create dictionary with key = module and value = semester_count
            modules_per_sem = dict(zip(sem_data[1], sem_data[5]))

            # create course dataframe
            courses = pd.DataFrame(course_list)

            # and map semester counts for each course to new column "semester"
            # this combines the information of the sem() atoms and the course() atoms
            courses['semester'] = courses[1].map(modules_per_sem)
            courses.drop([0,3,7,8], inplace=True, axis=1) # drop unneccessary information

            # create nested list with courses per semester
            courses_per_sem = []
            y = courses.groupby(["semester"])

            for key, item in y:
                # gives list of dataframes per sem and
                # creates list of semesters including all information
                courses_per_sem.append((y.get_group(key)).values.tolist())

            # gives nested list of courses per semester
            return courses_per_sem

        # convert information about courses per semester into timetable format (mon-fri, times)
        def timetable_multi(df_list):

            # create empty timetable dataframe
            timetable = pd.DataFrame(columns = ["mon", "tue","wed","thu","fri"])

            # create empty list for online courses
            online = []

            # add courses to timetable df
            for element in range(len(df_list)):

                # if element has label "0", it means that this course is taught online
                if df_list[element][2] == "0":
                    online.append(df_list[element][1]) # append course to online list

                # else, course has a time/day
                else:
                    # insert values at specific cells, i.e. start time, day
                    timetable.at[str(df_list[element][3]),str(df_list[element][2])] = df_list[element][1]
            try:
                # sort timetable wrt. times and weekdays
                timetable = timetable.fillna('').sort_index()
                #timetable = timetable[["0", "mon", "tue", "wed", "thu", "fri"]]
                timetable = timetable[["mon", "tue", "wed", "thu", "fri"]]
                # get list of courses abbreviations per timetable
                short_names = [x for x in np.unique(timetable.values)]

            # if we do not have a timetable (bc. we only have online courses), pass
            except:
                pass

            # return timetable dataframe and list of online courses
            return timetable, online


