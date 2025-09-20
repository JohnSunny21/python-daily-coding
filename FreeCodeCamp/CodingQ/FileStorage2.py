"""
File Storage
Given a file size, a unit for the file size, and hard drive capacity in gigabytes (GB), return the number of files the hard drive can store using the following constraints:

The unit for the file size can be bytes ("B"), kilobytes ("KB"), or megabytes ("MB").
Return the number of whole files the drive can fit.
Use the following conversions:
Unit	Equivalent
1 B	1 B
1 KB	1000 B
1 MB	1000 KB
1 GB	1000 MB
For example, given 500, "KB", and 1 as arguments, determine how many 500 KB files can fit on a 1 GB hard drive.



"""

def number_of_files(file_size, file_unit, drive_size_gb):

    if file_unit == "B":
        size_in_bytes = file_size
    elif file_unit == "KB":
        size_in_bytes = file_size * 1000
    elif file_unit == "MB":
        size_in_bytes = file_size * 1000 * 1000
    else:
        raise ValueError("Invalid unit. Use 'B', 'KB', or 'MB'.")
    

    drive_size_bytes = drive_size_gb * 1000 * 1000 * 1000
    return drive_size_bytes // size_in_bytes




if __name__ == "__main__":
    print(number_of_files(500,"KB",1))
    print(number_of_files(50000,"B",1))