"""
Photo Storage
Given a photo size in megabytes (MB), and hard drive capacity in gigabytes (GB), return the number of photos the hard drive can store using the following constraints:

1 gigabyte equals 1000 megabytes.
Return the number of whole photos the drive can store.
"""

def number_of_photos(photos_size_mb, drive_size_gb):

    drive_size_mb = drive_size_gb * 1000
    photos_size_mb = drive_size_mb // photos_size_mb
    return photos_size_mb


if __name__ == "__main__":
    print(number_of_photos(1,1))
    print(number_of_photos(2,1))
