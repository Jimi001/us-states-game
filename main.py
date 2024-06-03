import turtle
import pandas

# Function to set up the screen with the provided image
def setup_screen(image_path):
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    screen.addshape(image_path)
    turtle.shape(image_path)
    return screen

# Function to read state data from a CSV file and return a list of states and the data DataFrame
def get_state_data(file_path):
    data = pandas.read_csv(file_path)
    return data.state.to_list(), data

# Function to prompt the user for a state name
def prompt_user_for_state(screen, correct_count):
    return screen.textinput(title=f"{correct_count}/50 States Correct",
                            prompt="What's another state's name?").title()

# Function to mark the guessed state on the map
def mark_state_on_map(state_name, state_data):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_row = state_data[state_data.state == state_name]
    t.goto(int(state_row.x), int(state_row.y))
    t.write(state_name)

# Function to save the missing states to a CSV file
def save_missing_states(all_states, guessed_states, file_path):
    missing_states = [state for state in all_states if state not in guessed_states]
    pandas.DataFrame(missing_states).to_csv(file_path)

# Main function to coordinate the game setup and loop
def main():
    # Set up the game screen
    screen = setup_screen("blank_states_img.gif")
    
    # Load state data
    all_states, data = get_state_data("50_states.csv")
    
    guessed_states = []

    # Main game loop
    while len(guessed_states) < 50:
        # Prompt the user for a state name
        answer_state = prompt_user_for_state(screen, len(guessed_states))
        
        # If user wants to exit, save the missing states and break the loop
        if answer_state == "Exit":
            save_missing_states(all_states, guessed_states, "states_to_learn.csv")
            break
        
        # If the guessed state is correct and not already guessed, mark it on the map
        if answer_state in all_states and answer_state not in guessed_states:
            guessed_states.append(answer_state)
            mark_state_on_map(answer_state, data)

    # Wait for a click to close the screen
    screen.exitonclick()

if __name__ == "__main__":
    main()
