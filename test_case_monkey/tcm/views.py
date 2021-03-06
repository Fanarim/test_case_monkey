from . import models
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.shortcuts import get_object_or_404

# TODO check user permissions


class OrganisationList(ListView):
    template_name = 'organisation_list.html'
    model = models.Organisation
    context_object_name = 'organisations'


class OrganisationDetail(DetailView):
    template_name = 'organisation_detail.html'
    model = models.Organisation
    context_object_name = 'organisation'
    pk_url_kwarg = 'org_pk'

    def get_context_data(self, **kwargs):
        context = super(OrganisationDetail, self).get_context_data(**kwargs)
        return context


class ProjectDetail(DetailView):
    template_name = 'project_detail.html'
    model = models.Project
    context_object_name = 'project'
    pk_url_kwarg = 'project_pk'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetail, self).get_context_data(**kwargs)

        # check parent organisation exists, otherwise return 404
        parent_org = get_object_or_404(models.Organisation,
                                       name=self.kwargs['org_pk'])

        return context


class ProjectCreate(CreateView):
    template_name = 'project_create.html'
    model = models.Project

    fields = ['name', 'description']
    success_url = '..'

    def form_valid(self, form):
        form.instance.organisation = get_object_or_404(models.Organisation,
                                                       name=self.kwargs['org_pk'])
        return super(ProjectCreate, self).form_valid(form)


class ProjectEdit(UpdateView):
    template_name = 'project_edit.html'
    model = models.Project
    context_object_name = 'project'
    pk_url_kwarg = 'project_pk'

    fields = ['description']
    success_url = '../../..'

    def form_valid(self, form):
        form.instance.organisation = get_object_or_404(models.Organisation,
                                                       name=self.kwargs['org_pk'])
        return super(ProjectEdit, self).form_valid(form)


class ProjectDelete(DeleteView):
    template_name = 'project_delete.html'
    model = models.Project
    context_object_name = 'project'
    pk_url_kwarg = 'project_pk'
    success_url = '../../../'

    def form_valid(self, form):
        form.instance.organisation = get_object_or_404(models.Organisation,
                                                       name=self.kwargs['org_pk'])
        return super(ProjectDelete, self).form_valid(form)


class ScenarioTemplateDetail(DetailView):
    template_name = 'testscenariotemplate_detail.html'
    model = models.TestScenarioTemplate
    context_object_name = 'scenario'
    pk_url_kwarg = 'scenario_pk'

    def get_context_data(self, **kwargs):
        context = super(ScenarioTemplateDetail, self).get_context_data(**kwargs)

        # check if scenario is listed in given project and organisation,
        # otherwise return 404
        parent_project = get_object_or_404(models.Project,
                                           name=self.kwargs['project_pk'])
        parent_org = get_object_or_404(models.Organisation,
                                       name=self.kwargs['org_pk'])
        if parent_project not in parent_org.projects.all():
            pass
            # TODO return 404

        return context


class TestCaseTemplateDetail(DetailView):
    template_name = 'testcasetemplate_detail.html'
    model = models.TestCaseTemplate
    context_object_name = 'testcase'
    pk_url_kwarg = 'testcase_pk'

    def get_context_data(self, **kwargs):
        context = super(TestCaseTemplateDetail, self).get_context_data(**kwargs)

        # check if scenario is listed in given project and organisation,
        # otherwise return 404
        parent_scenario_template = get_object_or_404(
            models.TestScenarioTemplate,
            id=self.kwargs['scenario_pk'])
        parent_project = get_object_or_404(models.Project,
                                           name=self.kwargs['project_pk'])
        parent_org = get_object_or_404(models.Organisation,
                                       name=self.kwargs['org_pk'])
        if parent_scenario_template not in parent_project.scenarios.all():
            pass
            # TODO return 404
        if parent_project not in parent_org.projects.all():
            pass
            # TODO return 404

        return context


class TestRunDetail(DetailView):
    template_name = 'testrun_detail.html'
    model = models.TestRun
    context_object_name = 'testrun'
    pk_url_kwarg = 'testrun_pk'

    def get_context_data(self, **kwargs):
        context = super(TestRunDetail, self).get_context_data(**kwargs)

        # check if scenario is listed in given project and organisation,
        # otherwise return 404
        parent_project = get_object_or_404(models.Project,
                                           name=self.kwargs['project_pk'])
        parent_org = get_object_or_404(models.Organisation,
                                       name=self.kwargs['org_pk'])
        if parent_project not in parent_org.projects.all():
            pass
            # TODO return 404

        return context


class TestRunList(ListView):
    template_name = 'testrun_list.html'
    model = models.TestRun
    context_object_name = 'testruns'

    def get_context_data(self, **kwargs):
        context = super(TestRunList, self).get_context_data(**kwargs)

        # check if testrun is listed in given project and organisation,
        # otherwise return 404
        parent_project = get_object_or_404(models.Project,
                                           name=self.kwargs['project_pk'])
        parent_org = get_object_or_404(models.Organisation,
                                       name=self.kwargs['org_pk'])
        if parent_project not in parent_org.projects.all():
            pass
            # TODO return 404

        return context


class ScenarioDetail(DetailView):
    template_name = 'testscenario_detail.html'
    model = models.TestScenario
    context_object_name = 'scenario'
    pk_url_kwarg = 'scenario_pk'

    def get_context_data(self, **kwargs):
        context = super(ScenarioDetail, self).get_context_data(**kwargs)

        # check if scenario is listed in given project and organisation,
        # otherwise return 404
        parent_testrun = get_object_or_404(models.TestRun,
                                           id=self.kwargs['testrun_pk'])
        parent_project = get_object_or_404(models.Project,
                                           name=self.kwargs['project_pk'])
        parent_org = get_object_or_404(models.Organisation,
                                       name=self.kwargs['org_pk'])

        if parent_project not in parent_org.projects.all() \
                or parent_testrun not in parent_project.testruns.all():
            pass
            # TODO return 404

        return context
