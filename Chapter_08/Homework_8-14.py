def car_info(make, model, **info):
    info["make"] = make
    info["model"] = model
    return info

mustang_gt = car_info("Ford", "Mustang GT", convertable= True, color= "orange")
print(mustang_gt)