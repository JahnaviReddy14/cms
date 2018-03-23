from django.shortcuts import render
from django.views.generic import View
from details.forms import EmpForm
from django.http import HttpResponseRedirect
from details.models import Employee,EmpAddr
import json
# Create your views here.
class income(View):
    def get(self,request):
        return render(request,'display.html')

income1=income.as_view()

#class storing(View):
#    def post(self,request,*args,**kwargs):
#        data={}
#        form=EmpForm(request.POST)

#        if form.is_valid():
#            form.save()
#            data['saved']=True
#        else:
#            data['saved'] = False
#            print form.errors
#        return render(request, 'data.html')

#stored=storing.as_view()

class storing(View):
    def post(self,request,*args,**kwargs):
        data={}
        if request.method == 'POST':
            # #data1 = json.loads(request.body)
            # print data1
            # firstname = data1['FirstName']
            # lastname = data1['LastName']
            # phone_no = data1['Phone_No']
            # email = data1['Email']
            form1=EmpForm(request.POST)
            if form1.is_valid() :
                print form1.data
                address1 = form1.data.get('Address1', None)
                address2 = form1.data.get('Address2', None)
                emp=form1.save()
                EmpAddr.objects.create(Address1=address1,Address2=address2,Employee_id=emp.id)
                # print form1
                # emp_obj = form1
                # emp_detail = form2
                # emp_detail.employee_id = emp_obj.id
                # emp_detail.save()
                data['saved']=True
            else:
                data['saved'] = False
                print form1.errors
                # print form2.errors
        else:
            form1 = EmpForm(prefix="form1")
            # form2 = EmpAdrForm(prefix="form2")
        return render(request, 'data.html')

stored=storing.as_view()

