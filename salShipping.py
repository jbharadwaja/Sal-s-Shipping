weight = 41.5
cost_ground = 0
cost_drone = 0
cost_ground_premium = 125.0
# Ground Shipping

if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4 + 20
elif weight > 10:
  cost_ground = weight * 4.75 + 20

print("Ground Shipping: " + str(cost_ground))

# Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.5 + 0
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9 + 0
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12 + 0
elif weight > 10:
  cost_drone = weight * 14.25 + 0

print("Drone Shipping: " + str(cost_drone))

print("Premium Shipping: " +str(cost_ground_premium))