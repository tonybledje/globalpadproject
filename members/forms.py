from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'memberFName',
            'memberMidInitial',
            'memberLName',
            'memberAdmissionDate',
            'memberGender',
            'MemberMaritalStatus',
            'memberInPadSocial',
            'dateAdmitted',
            'MemberCellPhone',
            'memberHomePhone',
            'memberAddress',
            'memberCity',
            'memberState',
            'memberZip',
            ]