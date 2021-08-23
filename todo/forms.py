from django import forms
from django.contrib.auth.models import Group
from django.forms import ModelForm
from todo.models import Task, TaskList
from usuarios.models import *
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

class AddTaskListForm(ModelForm):
    """The picklist showing allowable groups to which a new list can be added
    determines which groups the user belongs to. This queries the form object
    to derive that list."""

    def __init__(self, user, *args, **kwargs):
        super(AddTaskListForm, self).__init__(*args, **kwargs)
        

    class Meta:
        model = TaskList
        exclude = ["created_date", "slug"]


class AddEditTaskForm(ModelForm):
    """The picklist showing the users to which a new task can be assigned
    must find other members of the group this TaskList is attached to."""

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        task_list = kwargs.get("initial").get("task_list")
        # members = task_list.group.user_set.all()
        usuarios = Usuario.objects.all()
        self.fields["assigned_to"].queryset = usuarios
        self.fields["assigned_to"].label_from_instance = lambda obj: "%s" % (
            obj.nomb_usr,
        )
        self.fields["assigned_to"].widget.attrs = {
            "id": "id_assigned_to",
            "class": "custom-select mb-3",
            "name": "assigned_to",
        }
        self.fields["task_list"].value = kwargs["initial"]["task_list"].id

    # due_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type": "date"}), required=False)
    due_date = forms.DateTimeField(
        widget=DateTimePicker(
            options={
                'useCurrent': True,
                'collapse': False,
                'locale': 'es',
                'format': 'YYYY-MM-DD HH:mm',
                'enabledHours': [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            },
            attrs={
                'append': 'fa fa-calendar',
                
            }
        ), required=True
    )
    title = forms.CharField(widget=forms.widgets.TextInput())

    note = forms.CharField(widget=forms.Textarea(), required=False)

    completed = forms.BooleanField(required=False)

    def clean_created_by(self):
        """Keep the existing created_by regardless of anything coming from the submitted form.
        If creating a new task, then created_by will be None, but we set it before saving."""
        return self.instance.created_by

    class Meta:
        model = Task
        exclude = []


class AddExternalTaskForm(ModelForm):
    """Form to allow users who are not part of the GTD system to file a ticket."""

    title = forms.CharField(widget=forms.widgets.TextInput(attrs={"size": 35}), label="Summary")
    note = forms.CharField(widget=forms.widgets.Textarea(), label="Problem Description")
    priority = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Task
        exclude = (
            "task_list",
            "created_date",
            "due_date",
            "created_by",
            "assigned_to",
            "completed",
            "completed_date",
        )


class SearchForm(forms.Form):
    """Search."""

    q = forms.CharField(widget=forms.widgets.TextInput(attrs={"size": 35}))
