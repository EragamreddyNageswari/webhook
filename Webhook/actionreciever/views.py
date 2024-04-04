from django.shortcuts import render

# Create your views here.

def home(request):
    webhookdata = {}
    return render(request,'home.html',webhookdata)


def receiver(request):
    if request.method == 'POST':
        # Assuming you're using Django or a similar web framework
        github_data = request.POST.get(
            'github_data')  # Assuming the GitHub webhook data is sent as a parameter named 'github_data'

        # Save the GitHub webhook data into MongoDB
        # Example code assuming you're using pymongo
        import pymongo
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["mydatabase"]
        collection = db["github_webhook_data"]
        collection.insert_one({"github_data": github_data})

        # Respond with a success message or appropriate HTTP response
        return HttpResponse("Data received and saved successfully!", status=200)
    else:
        # Handle other HTTP methods if necessary
        return HttpResponse("Method not allowed", status=405)
