"""
    Pure1 Public REST API

    Pure1 Public REST API, developed by [Pure Storage, Inc.](https://www.purestorage.com)   The Pure1 REST API 2.0 offers one single form of authentication: OAuth 2.0 via the [Token Exchange protocol](https://datatracker.ietf.org/doc/draft-ietf-oauth-token-exchange).  OAuth 2.0 is an open protocol to allow secure authorization in a simple and standard method from web, mobile, desktop and background applications.  Note that the [Authentication](#section/Authentication) section below mentions 'API Key' as the security scheme type. This is solely for the purpose of allowing testing this API with [Swagger UI](https://static.pure1.purestorage.com/api-swagger/index.html).  [Knowledge base reference documentation](https://support.purestorage.com/Pure1/Pure1_Manage/Pure1_Manage_-_REST_API/Pure1_Manage_-_REST_API__Reference)

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


class __LazyApiLoader:
    def __init__(self, modname, attr):
        self._modname  = modname
        self._attr     = attr
        self._mod      = None

    def load(self):
        import importlib
        if self._mod is None:
            self._mod = importlib.__import__(self._modname, globals(), locals(), fromlist=[self._attr], level=1)
        return getattr(self._mod, self._attr)

__class_apis_dict = { 
    'AlertsApi': __LazyApiLoader('alerts_api', 'AlertsApi'),
    'ArraysApi': __LazyApiLoader('arrays_api', 'ArraysApi'),
    'AuditsApi': __LazyApiLoader('audits_api', 'AuditsApi'),
    'AuthorizationApi': __LazyApiLoader('authorization_api', 'AuthorizationApi'),
    'BladesApi': __LazyApiLoader('blades_api', 'BladesApi'),
    'BucketReplicaLinksApi': __LazyApiLoader('bucket_replica_links_api', 'BucketReplicaLinksApi'),
    'BucketsApi': __LazyApiLoader('buckets_api', 'BucketsApi'),
    'ControllersApi': __LazyApiLoader('controllers_api', 'ControllersApi'),
    'DirectoriesApi': __LazyApiLoader('directories_api', 'DirectoriesApi'),
    'DrivesApi': __LazyApiLoader('drives_api', 'DrivesApi'),
    'FileSystemReplicaLinksApi': __LazyApiLoader('file_system_replica_links_api', 'FileSystemReplicaLinksApi'),
    'FileSystemSnapshotsApi': __LazyApiLoader('file_system_snapshots_api', 'FileSystemSnapshotsApi'),
    'FileSystemsApi': __LazyApiLoader('file_systems_api', 'FileSystemsApi'),
    'HardwareApi': __LazyApiLoader('hardware_api', 'HardwareApi'),
    'HardwareConnectorsApi': __LazyApiLoader('hardware_connectors_api', 'HardwareConnectorsApi'),
    'InvoicesApi': __LazyApiLoader('invoices_api', 'InvoicesApi'),
    'MetricsApi': __LazyApiLoader('metrics_api', 'MetricsApi'),
    'NetworkInterfacesApi': __LazyApiLoader('network_interfaces_api', 'NetworkInterfacesApi'),
    'ObjectStoreAccountsApi': __LazyApiLoader('object_store_accounts_api', 'ObjectStoreAccountsApi'),
    'PodReplicaLinksApi': __LazyApiLoader('pod_replica_links_api', 'PodReplicaLinksApi'),
    'PodsApi': __LazyApiLoader('pods_api', 'PodsApi'),
    'PoliciesApi': __LazyApiLoader('policies_api', 'PoliciesApi'),
    'PortsApi': __LazyApiLoader('ports_api', 'PortsApi'),
    'SubscriptionsApi': __LazyApiLoader('subscriptions_api', 'SubscriptionsApi'),
    'SustainabilityApi': __LazyApiLoader('sustainability_api', 'SustainabilityApi'),
    'TargetsApi': __LazyApiLoader('targets_api', 'TargetsApi'),
    'VolumeSnapshotsApi': __LazyApiLoader('volume_snapshots_api', 'VolumeSnapshotsApi'),
    'VolumesApi': __LazyApiLoader('volumes_api', 'VolumesApi'),
}

def __getattr__(name, default=None):
    if '_apis_list' == name:
        return __class_apis_dict.keys()
    if name not in __class_apis_dict:
        raise AttributeError(f'module {__name__} has no attribute {name}')
    return __class_apis_dict[name].load()
