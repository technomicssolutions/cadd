from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.conf import settings

from fees.views import CreateFeesStructure, EditFeesStructure, DeleteFeesStructure, ListFeesStructure, AddFeesHead, EditFeesHead, \
	DeleteFeesHead, FeesHeadList, FeesPaymentSave, GetFeeStructureHeadList, ListOutStandingFees, CommonFeesPaymentSave, \
	GetFeesHeadList, GetOutStandingFeesDetails, PrintOutstandingFeesReport, FeepaymentReport, UnRollStudent, RollStudent

urlpatterns = patterns('',
	url(r'^fees_heads/$',login_required(FeesHeadList.as_view()), name='fees_heads'),
	url(r'^add_fees_head/$',login_required(AddFeesHead.as_view()), name='add_fees_head'),
	url(r'^edit_fees_head/(?P<fees_head_id>\d+)/$', login_required(EditFeesHead.as_view()), name='edit_fees_head'),
	url(r'^delete_fees_head/(?P<fees_head_id>\d+)/$', login_required(DeleteFeesHead.as_view()), name='delete_fees_head'),
	
	url(r'^fees_structures/$',login_required(ListFeesStructure.as_view()), name='list_fees_structure'),
	url(r'^new_fees_structure/$',login_required(CreateFeesStructure.as_view()), name='new_fees_structure'),
	url(r'^delete_fees_structure_details/(?P<fees_structure_id>\d+)/$',login_required(DeleteFeesStructure.as_view()), name="delete_fees_structure_details"),
	url(r'^edit_fees_structure_details/(?P<fees_structure_id>\d+)/$',login_required(EditFeesStructure.as_view()), name="edit_fees_structure_details"),

	url(r'^fees_payment/$',login_required(FeesPaymentSave.as_view()), name='fees_payment'),
	url(r'^common_fees_payment/$',login_required(CommonFeesPaymentSave.as_view()), name='common_fees_payment'),
	
	url(r'^get_fee_structure_head/(?P<course_id>\d+)/(?P<batch_id>\d+)/(?P<student_id>\d+)/$',login_required(GetFeeStructureHeadList.as_view()), name='get_fee_structure_head'),
	url(r'^get_common_fees_head/(?P<course_id>\d+)/(?P<batch_id>\d+)/(?P<student_id>\d+)/$',login_required(GetFeesHeadList.as_view()), name='get_fee_structure_head'),
	
	url(r'^list_outstanding_fees/$',login_required(ListOutStandingFees.as_view()), name='list_outstanding_fees'),
	url(r'^get_outstanding_fees_details/$',login_required(GetOutStandingFeesDetails.as_view()), name='get_outstanding_fees_details'),
	
	url(r'^print_outstanding_fees_details/$', login_required(PrintOutstandingFeesReport.as_view()), name='print_outstanding_fees_details'),
	url(r'^fees_payment_report/$', login_required(FeepaymentReport.as_view()), name='fees_payment_report'),
	url(r'^unroll_students/$',login_required(UnRollStudent.as_view()), name='unroll_students'),
	url(r'^roll_students/$',login_required(RollStudent.as_view()), name='roll_students'),
)