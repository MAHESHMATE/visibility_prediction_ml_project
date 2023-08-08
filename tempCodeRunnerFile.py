
        if request.json is not None:
            path = request.json['filepath']

            pred_val = pred_validation(path) #object initialization