%global pkg_name munge-maven-plugin
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.0
Release:        2.9%{?dist}
Summary:        Munge Maven Plugin
License:        CDDL
URL:            http://github.com/sonatype/munge-maven-plugin
BuildArch:      noarch

Source0:        https://github.com/sonatype/munge-maven-plugin/archive/munge-maven-plugin-1.0.tar.gz

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix}sonatype-plugins-parent

%description
Munge is a purposely-simple Java preprocessor. It only supports
conditional inclusion of source based on defined strings of the
form "if[tag]", "if_not[tag]", "else[tag]", and "end[tag]".
Unlike traditional preprocessors, comments, and formatting are all
preserved for the included lines. This is on purpose, as the output
of Munge will be distributed as human-readable source code.

To avoid creating a separate Java dialect, the conditional tags are
contained in Java comments. This allows one build to compile the
source files without pre-processing, to facilitate faster incremental
development. Other builds from the same source have their code contained
within that comment. The format of the tags is a little verbose, so
that the tags won't accidentally be used by other comment readers
such as javadoc. Munge tags must be in C-style comments;
C++-style comments may be used to comment code within a comment.

Like any preprocessor, developers must be careful not to abuse its
capabilities so that their code becomes unreadable. Please use it
as little as possible.

%package javadoc
Summary:        API documentation for %{pkg_name}

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{pkg_name}-%{pkg_name}-%{version}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE README

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-2.9
- Add directory ownership on %%{_mavenpomdir} subdir

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.0-2.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.0-2.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-2.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-2.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-2.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-2.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-2.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-2.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0-2
- Mass rebuild 2013-12-27

* Tue Sep 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-1
- Initial packaging
