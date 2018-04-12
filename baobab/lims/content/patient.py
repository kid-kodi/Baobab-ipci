"""Product Category
Category of the product, for example, sampling containers and sampling
kits.
"""
from AccessControl import ClassSecurityInfo
from Products.ATContentTypes.content import schemata
from Products.Archetypes.atapi import *
from Products.CMFPlone.interfaces import IConstrainTypes
from plone.indexer import indexer
from zope.interface import implements
from Products.CMFCore import permissions
from plone.app.folder.folder import ATFolder
from Products.CMFCore.utils import getToolByName
from Products.Archetypes.references import HoldingReference
from DateTime import DateTime

from bika.lims.browser.widgets import DateTimeWidget
from bika.lims.content.bikaschema import BikaSchema, BikaFolderSchema
from bika.lims.browser.widgets import ReferenceWidget as bika_ReferenceWidget
from baobab.lims import bikaMessageFactory as _
from baobab.lims.interfaces import IPatient, IPatients
from baobab.lims.config import PROJECTNAME

PatientID = StringField(
    'PatientID',
    required=1,
    searchable=True,
    mode="rw",
    widget=StringWidget(
        label=_("PatientID"),
        visible={'edit': 'visible', 'view': 'visible'}
    ),
)

FirstName = StringField(
    'FirstName',
    required=1,
    searchable=True,
    mode="rw",
    widget=StringWidget(
        label=_("First Name"),
        visible={'edit': 'visible', 'view': 'visible'}
    ),
)

LastName = StringField(
    'LastName',
    required=1,
    searchable=True,
    mode="rw",
    widget=StringWidget(
        label=_("Last Name"),
        visible={'edit': 'visible', 'view': 'visible'}
    ),
)

schema = BikaSchema.copy() + Schema((
    PatientID,
    FirstName,
    LastName
))

schema['title'].widget.visible = {'view': 'invisible', 'edit': 'invisible'}
schema['description'].widget.visible = {'view': 'invisible', 'edit': 'invisible'}


class Patient(BaseContent):
    security = ClassSecurityInfo()
    implements(IPatient)
    displayContentsTab = False
    schema = schema
    _at_rename_after_creation = True

    def Title(self):
        return self.getPatientID()

    def Description(self):
        return self.getFirstName() + ' ' + self.getLastName()

registerType(Patient, PROJECTNAME)