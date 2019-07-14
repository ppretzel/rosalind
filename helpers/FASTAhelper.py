# Helper functions to handle FASTA files

def readFASTA(filepath):

    with open(filepath, "r") as f:
        lines = f.readlines()

    # result_dict will contain all strings and associated keys
    result_dict = {}

    current_id = None
    current_string = ""

    for line in lines:
        
        # handle a new ID
        if line.startswith(">"):

            # store last processed ID and string in result dict
            if current_id != None:
                result_dict[current_id.strip()] = current_string.strip()
                current_string = ""

            # store new id without the leading '>'
            current_id = line[1:].strip()

        # otherwise just append the line
        else:

            current_string += line.strip()

    # don't forget to push the last element after having finished the iteration
    result_dict[current_id.strip()] = current_string.strip()

    return result_dict
