var chartExample = {
    initChart: function (data) {

        var ndx = crossfilter(data),
            teamMemberDimension = ndx.dimension(function (d) {
                return d.teamMember;
            }),
            teamMemberChart = dc.rowChart("#teammateChart"),
            teamMemberGroup = teamMemberDimension.group().reduce(

            function (p, d) {
                if (d.project in p.projects) p.projects[d.project]++;
                else {
                    p.projects[d.project] = 1;
                    p.projectCount++;
                }
                return p;
            },

            function (p, d) {
                p.projects[d.project]--;
                if (p.projects[d.project] === 0) {
                    delete p.projects[d.project];
                    p.projectCount--;
                }
                return p;
            },

            function () {
                return {
                    projectCount: 0,
                    projects: {}
                };
            });
        teamMemberChart
            .width(270)
            .height(220)
            .dimension(teamMemberDimension)
            .group(teamMemberGroup)
            .valueAccessor(function (d) {
            return d.value.projectCount;
        })
            .elasticX(true);
        
        dc.renderAll();
    },
    initData: function () {
        var projectActions = [{
            project: "Website Hosting",
            teamMember: "Sam",
            action: "email"
        }, {
            project: "Website Hosting",
            teamMember: "Sam",
            action: "phoneCall"
        }, {
            project: "Budjet",
            teamMember: "Joe",
            action: "email"
        }, {
            project: "Website Design",
            teamMember: "Joe",
            action: "design"
        }, {
            project: "Budget",
            teamMember: "Sam",
            action: "email"
        }, {
            project: "Foo",
            teamMember: "Sam",
            action: "email"
        }];
        chartExample.initChart(projectActions);
    }
};

chartExample.initData();