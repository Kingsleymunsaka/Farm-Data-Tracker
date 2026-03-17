# Step 2: Farm Data Tracker – Multiple Crops
crop_data = {"corn": 3.95, "cassava": 4.0, "wheat": 2.8}  # yield per hectare

number_of_crops = int(input("How many crops do you want to enter? "))
total_results = {}

for i in range(number_of_crops):
    crop = input("Enter crop name (corn/cassava/wheat): ").lower()
    area = float(input("Enter area in hectares: "))
    
    if crop in crop_data:
        estimated_yield = area * crop_data[crop]
        total_results[crop] = estimated_yield
    else:
        print("Sorry, crop not in database.")

print("\n--- Farm Summary ---")
for crop, yield_amount in total_results.items():
    print(crop.capitalize(), ":", yield_amount, "tonnes")