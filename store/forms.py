from django.contrib.auth import password_validation
# from store.models import Address
from .models import *
from django import forms
import django
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.db import models
from django.db.models import fields
from django.forms import widgets
from django.forms.fields import CharField
from django.utils.translation import gettext, gettext_lazy as _



class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {'email': 'Email', 'First name': 'first_name', 'Last name': 'last_name'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['locality', 'city', 'state']
        widgets = {'locality':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Popular Place like Restaurant, Religious Site, etc.'}), 'city':forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}), 'state':forms.TextInput(attrs={'class':'form-control', 'placeholder':'State or Province'})}


class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'auto-focus':True, 'class':'form-control', 'placeholder':'Current Password'}))
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control', 'placeholder':'New Password'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control', 'placeholder':'Confirm Password'}))


class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete':'email', 'class':'form-control'}))


class SetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))


class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = [
            'title',
            'description',
            'location',
            'category',
            'job_type',
            'salary',
            'years_of_experience_required',
            'certification_required',
            'skills_required',
            'company_name',
            'company_email',
            'company_phone',
            'company_website',
            'application_deadline'
        ]
        labels = {
            'title': 'Job Title',
            'description': 'Job Description',
            'location': 'Job Location',
            'category': 'Job Category',
            'job_type': 'Job Type',
            'salary': 'Salary',
            'years_of_experience_required': 'Years of Experience Required',
            'certification_required': 'Certification Required',
            'skills_required': 'Skills Required',
            'company_name': 'Company Name',
            'company_email': 'Contact Email',
            'company_phone': 'Contact Phone',
            'company_website': 'Company Website',
            'application_deadline': 'Application Deadline',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Job Description'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Location'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'job_type': forms.Select(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
            'years_of_experience_required': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Years of Experience'}),
            'certification_required': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'skills_required': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'company_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Contact Email'}),
            'company_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Phone'}),
            'company_website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Company Website'}),
            'application_deadline': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Application Deadline', 'type': 'date'}),
        }


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'applicant_first_name',
            'applicant_last_name',
            'applicant_email',
            'applicant_phone_number',
            'applicant_address',
            'applicant_desired_position',
            'applicant_years_of_experience',
            'applicant_is_certified_operator',
            'applicant_certifications',
            'applicant_skills',
            'applicant_resume',
            'applicant_cover_letter'
        ]
        widgets = {
            'applicant_first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'applicant_last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'applicant_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'applicant_phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'applicant_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address', 'rows': 3}),
            'applicant_desired_position': forms.Select(attrs={'class': 'form-control'}),
            'applicant_years_of_experience': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Years of Experience'}),
            'applicant_is_certified_operator': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'applicant_certifications': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Certifications', 'rows': 3}),
            'applicant_skills': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'applicant_resume': forms.FileInput(attrs={'class': 'form-control'}),
            'applicant_cover_letter': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Cover Letter', 'rows': 5}),
        }
        labels = {
            'applicant_first_name': 'First Name',
            'applicant_last_name': 'Last Name',
            'applicant_email': 'Email Address',
            'applicant_phone_number': 'Phone Number',
            'applicant_address': 'Address',
            'applicant_desired_position': 'Desired Position',
            'applicant_years_of_experience': 'Years of Experience',
            'applicant_is_certified_operator': 'Certified Tractor Operator',
            'applicant_certifications': 'Relevant Certifications',
            'applicant_skills': 'Skills and Expertise',
            'applicant_resume': 'Upload Resume (PDF or DOC)',
            'applicant_cover_letter': 'Cover Letter',
        }


class TractorOperatorForm(forms.ModelForm):
    class Meta:
        model = TractorOperator
        fields = [
            'operator_first_name',
            'operator_last_name',
            'operator_phone_number',
            'operator_email',
            'operator_profile_picture',
            'operator_category',
            'operator_subcategory',
            'operator_experience_years',
            'operator_tractor_models_operated',
            'operator_address',
        ]
        widgets = {
            'operator_first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'operator_last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'operator_phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'operator_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'operator_profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
            'operator_category': forms.Select(attrs={'class': 'form-control'}),
            'operator_subcategory': forms.Select(attrs={'class': 'form-control'}),
            'operator_experience_years': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Years of Experience'}),
            'operator_tractor_models_operated': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tractor Models Operated', 'rows': 3}),
            'operator_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address', 'rows': 3}),
        }
        labels = {
            'operator_first_name': 'First Name',
            'operator_last_name': 'Last Name',
            'operator_phone_number': 'Phone Number',
            'operator_email': 'Email Address',
            'operator_profile_picture': 'Profile Picture',
            'operator_category': 'Category',
            'operator_subcategory': 'Subcategory',
            'operator_experience_years': 'Years of Experience',
            'operator_tractor_models_operated': 'Tractor Models Operated',
            'operator_address': 'Address',
        }
