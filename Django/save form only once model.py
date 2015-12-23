
#views.py
class CustomerServieViews(object):
	def customer_service(self, request):
		if request.user.is_anonymous():
			return HttpResponseRedirect('/accounts/login')
		try:
			customer_service = models.Customer_Service.objects.get(pk=models.Customer_Service.objects.all()[0].id)
		except:
			customer_service = models.Customer_Service()

		Data_Bank_FormSet = inlineformset_factory(models.Customer_Service, models.Data_Bank_Customer_Service, form=Data_Bank_Customer_Service_Form, extra=1, can_delete=False)
		
		if request.method == 'GET':
			form 				= Customer_Service_Form(instance=customer_service)
			formset_data_bank 	= Data_Bank_FormSet(instance=customer_service)
		else:
			form 				= Customer_Service_Form(request.POST, instance=customer_service)
			formset_data_bank 	= Data_Bank_FormSet(request.POST, instance=customer_service)
			if form.is_valid() and formset_data_bank.is_valid():
				formset_data_bank.save()
				form.save()

				success_msg = "Data Customer Service Berhasil Update."
				get_model_id = models.Customer_Service.objects.get(pk=models.Customer_Service.objects.all()[0].id)
				form = Customer_Service_Form(request.POST, instance=get_model_id)
				formset_data_bank = Data_Bank_FormSet(request.POST, instance=get_model_id)

				args = {
						'formset_data_bank': formset_data_bank,
						'user': request.user, 
						'request': request, 
						'success_msg': success_msg
						}
				args.update(csrf(request))
				args['form'] = form

				return render_to_response('new_edit_admin_customer_service.html', args)
		
		args = {
				'formset_data_bank': formset_data_bank,
				'user': request.user, 
				'request': request
				}
		args.update(csrf(request))
		args['form'] = form
		return render_to_response('new_edit_admin_customer_service.html', args)
