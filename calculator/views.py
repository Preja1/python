from django.shortcuts import render
from calculator.models import CalculatorHistory

# Create your views here.

def calculate_view(request):
     # result = None
    # number_a = ''
    # number_b = ''

    # if request.method == 'POST':
    #     try:
    #         number_a = float(request.POST.get('number_a',0))
    #         number_b = float(request.POST.get('number_b',0))
    #         result = number_a + number_b
    #     except(ValueError,TypeError):
    #         result = 'Invalid input'
    #     return render(request,'calc.html',{ 'sum':result})

    # return render(request,'calculator.html')
    context = {}
    data={}

    if request.method == "POST":
        form_data = request.POST
        number_a = form_data.get("number_a")
        number_b = form_data.get("number_b")

        operation = list(form_data.keys())[-1]

        if number_a.isnumeric() and number_b.isnumeric():
            number_a = float(number_a)
            number_b = float(number_b)
            data.update(
                number_a=number_a,
                number_b=number_b
            )

            action = ""
            message = ""

            if "add" in operation:
                total = number_a + number_b
                action = "add"
                context.update(
                    message=f"Addition of {number_a} and {number_b} is : {total}"
                )

            elif "sub" in operation:
                total = number_a - number_b
                action = "sub"
                message = f"Subtraction of {number_a} and {number_b} is : {total}"
                context.update(
                    message=message
                )

            elif "multi" in operation:
                total = number_a * number_b
                action = "multi"
                message = f"Product of {number_a} and {number_b} is : {total}"
                context.update(
                    message=message
                )

            elif "div" in operation:
                if number_b == 0:
                    message = f"Denominator must be nonzero!"
                    context.update(
                        message=message
                    )
                else:
                    total = number_a / number_b
                    action = "div"
                    message = f"Quotient of {number_a} and {number_b} is : {total}"
                    context.update(
                        message=message
                    )

            data.update(
                        operation=action,
                        operation_status="Success",
                        result=message
                    )
            CalculatorHistory.objects.create(**data)

    else:
         context.update(message="You need to pass numeric values!")

    return render(request, "calculator.html", context)

