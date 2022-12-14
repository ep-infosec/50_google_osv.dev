# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from osv import deps_dev_pb2 as osv_dot_deps__dev__pb2


class InsightsStub(object):
    """Add a go_package that places the generated files in your own package.
    Example:
    option go_package = "github.com/myname/deps.dev/api";
    The Insights service is served by api.deps.dev:443 using gRPC.

    This is not yet a stable service, and the protocol is subject to change.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Packages = channel.unary_stream(
                '/deps_dev.v2alpha.Insights/Packages',
                request_serializer=osv_dot_deps__dev__pb2.PackagesRequest.SerializeToString,
                response_deserializer=osv_dot_deps__dev__pb2.PackagesResponse.FromString,
                )
        self.Versions = channel.unary_stream(
                '/deps_dev.v2alpha.Insights/Versions',
                request_serializer=osv_dot_deps__dev__pb2.VersionsRequest.SerializeToString,
                response_deserializer=osv_dot_deps__dev__pb2.VersionsResponse.FromString,
                )
        self.Version = channel.unary_stream(
                '/deps_dev.v2alpha.Insights/Version',
                request_serializer=osv_dot_deps__dev__pb2.VersionRequest.SerializeToString,
                response_deserializer=osv_dot_deps__dev__pb2.VersionResponse.FromString,
                )
        self.Dependencies = channel.unary_stream(
                '/deps_dev.v2alpha.Insights/Dependencies',
                request_serializer=osv_dot_deps__dev__pb2.DependenciesRequest.SerializeToString,
                response_deserializer=osv_dot_deps__dev__pb2.DependenciesResponse.FromString,
                )
        self.DependentInfo = channel.unary_unary(
                '/deps_dev.v2alpha.Insights/DependentInfo',
                request_serializer=osv_dot_deps__dev__pb2.DependentInfoRequest.SerializeToString,
                response_deserializer=osv_dot_deps__dev__pb2.DependentInfoResponse.FromString,
                )
        self.Advisory = channel.unary_unary(
                '/deps_dev.v2alpha.Insights/Advisory',
                request_serializer=osv_dot_deps__dev__pb2.AdvisoryRequest.SerializeToString,
                response_deserializer=osv_dot_deps__dev__pb2.AdvisoryResponse.FromString,
                )
        self.Project = channel.unary_unary(
                '/deps_dev.v2alpha.Insights/Project',
                request_serializer=osv_dot_deps__dev__pb2.ProjectRequest.SerializeToString,
                response_deserializer=osv_dot_deps__dev__pb2.ProjectResponse.FromString,
                )
        self.ProjectPackageVersions = channel.unary_stream(
                '/deps_dev.v2alpha.Insights/ProjectPackageVersions',
                request_serializer=osv_dot_deps__dev__pb2.ProjectPackageVersionsRequest.SerializeToString,
                response_deserializer=osv_dot_deps__dev__pb2.ProjectPackageVersionsResponse.FromString,
                )


class InsightsServicer(object):
    """Add a go_package that places the generated files in your own package.
    Example:
    option go_package = "github.com/myname/deps.dev/api";
    The Insights service is served by api.deps.dev:443 using gRPC.

    This is not yet a stable service, and the protocol is subject to change.
    """

    def Packages(self, request, context):
        """Packages returns a list of all known packages, in a batched stream.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Versions(self, request, context):
        """Versions returns the versions of a package.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Version(self, request, context):
        """Version returns information about specific package versions. If the
        request matches more than one version, multiple responses are returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Dependencies(self, request, context):
        """Dependencies returns the full dependency graph of a package version, as a
        stream of messages containing nodes and edges. The first node in the
        stream is the root of the graph. Edges do not appear before their
        referenced nodes. If the request matches more than one version, an error
        is returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DependentInfo(self, request, context):
        """DependentInfo returns information about the dependents of a package
        version. If the request matches more than one version, an error is
        returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Advisory(self, request, context):
        """Advisory returns information about a security advisory.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Project(self, request, context):
        """Project returns information about the specified project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProjectPackageVersions(self, request, context):
        """ProjectPackageVersions returns a list of versions that reference the
        specified project.
        The links are not confirmed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InsightsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Packages': grpc.unary_stream_rpc_method_handler(
                    servicer.Packages,
                    request_deserializer=osv_dot_deps__dev__pb2.PackagesRequest.FromString,
                    response_serializer=osv_dot_deps__dev__pb2.PackagesResponse.SerializeToString,
            ),
            'Versions': grpc.unary_stream_rpc_method_handler(
                    servicer.Versions,
                    request_deserializer=osv_dot_deps__dev__pb2.VersionsRequest.FromString,
                    response_serializer=osv_dot_deps__dev__pb2.VersionsResponse.SerializeToString,
            ),
            'Version': grpc.unary_stream_rpc_method_handler(
                    servicer.Version,
                    request_deserializer=osv_dot_deps__dev__pb2.VersionRequest.FromString,
                    response_serializer=osv_dot_deps__dev__pb2.VersionResponse.SerializeToString,
            ),
            'Dependencies': grpc.unary_stream_rpc_method_handler(
                    servicer.Dependencies,
                    request_deserializer=osv_dot_deps__dev__pb2.DependenciesRequest.FromString,
                    response_serializer=osv_dot_deps__dev__pb2.DependenciesResponse.SerializeToString,
            ),
            'DependentInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.DependentInfo,
                    request_deserializer=osv_dot_deps__dev__pb2.DependentInfoRequest.FromString,
                    response_serializer=osv_dot_deps__dev__pb2.DependentInfoResponse.SerializeToString,
            ),
            'Advisory': grpc.unary_unary_rpc_method_handler(
                    servicer.Advisory,
                    request_deserializer=osv_dot_deps__dev__pb2.AdvisoryRequest.FromString,
                    response_serializer=osv_dot_deps__dev__pb2.AdvisoryResponse.SerializeToString,
            ),
            'Project': grpc.unary_unary_rpc_method_handler(
                    servicer.Project,
                    request_deserializer=osv_dot_deps__dev__pb2.ProjectRequest.FromString,
                    response_serializer=osv_dot_deps__dev__pb2.ProjectResponse.SerializeToString,
            ),
            'ProjectPackageVersions': grpc.unary_stream_rpc_method_handler(
                    servicer.ProjectPackageVersions,
                    request_deserializer=osv_dot_deps__dev__pb2.ProjectPackageVersionsRequest.FromString,
                    response_serializer=osv_dot_deps__dev__pb2.ProjectPackageVersionsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'deps_dev.v2alpha.Insights', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Insights(object):
    """Add a go_package that places the generated files in your own package.
    Example:
    option go_package = "github.com/myname/deps.dev/api";
    The Insights service is served by api.deps.dev:443 using gRPC.

    This is not yet a stable service, and the protocol is subject to change.
    """

    @staticmethod
    def Packages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/deps_dev.v2alpha.Insights/Packages',
            osv_dot_deps__dev__pb2.PackagesRequest.SerializeToString,
            osv_dot_deps__dev__pb2.PackagesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Versions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/deps_dev.v2alpha.Insights/Versions',
            osv_dot_deps__dev__pb2.VersionsRequest.SerializeToString,
            osv_dot_deps__dev__pb2.VersionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Version(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/deps_dev.v2alpha.Insights/Version',
            osv_dot_deps__dev__pb2.VersionRequest.SerializeToString,
            osv_dot_deps__dev__pb2.VersionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Dependencies(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/deps_dev.v2alpha.Insights/Dependencies',
            osv_dot_deps__dev__pb2.DependenciesRequest.SerializeToString,
            osv_dot_deps__dev__pb2.DependenciesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DependentInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/deps_dev.v2alpha.Insights/DependentInfo',
            osv_dot_deps__dev__pb2.DependentInfoRequest.SerializeToString,
            osv_dot_deps__dev__pb2.DependentInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Advisory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/deps_dev.v2alpha.Insights/Advisory',
            osv_dot_deps__dev__pb2.AdvisoryRequest.SerializeToString,
            osv_dot_deps__dev__pb2.AdvisoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Project(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/deps_dev.v2alpha.Insights/Project',
            osv_dot_deps__dev__pb2.ProjectRequest.SerializeToString,
            osv_dot_deps__dev__pb2.ProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ProjectPackageVersions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/deps_dev.v2alpha.Insights/ProjectPackageVersions',
            osv_dot_deps__dev__pb2.ProjectPackageVersionsRequest.SerializeToString,
            osv_dot_deps__dev__pb2.ProjectPackageVersionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
