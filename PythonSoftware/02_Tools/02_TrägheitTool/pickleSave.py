# Store data into pickle
import pickle
 
class MyClass():
    def __init__(self, param):
        self.param = param
 
def save_object(obj):
    try:
        with open("data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)
 

# Create an object of the class MyClass
obj = MyClass(10)
# Save the created object into pickles
save_object(obj)
