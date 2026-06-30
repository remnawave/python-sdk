"""Tests that all required endpoints exist in controllers."""
import pytest
import inspect

from remnawave.controllers.users import UsersController
from remnawave.controllers.system import SystemController
from remnawave.controllers.ip_control import IpControlController
from remnawave.controllers.api_tokens_management import APITokensManagementController
from remnawave.controllers.hosts_bulk_actions import HostsBulkActionsController
from remnawave.controllers.bandwidthstats import BandWidthStatsController


class TestUsersControllerEndpoints:
    def test_has_resolve_user(self):
        assert hasattr(UsersController, "resolve_user")
        assert callable(getattr(UsersController, "resolve_user"))

    def test_has_revoke_user_subscription(self):
        assert hasattr(UsersController, "revoke_user_subscription")

    def test_has_disable_user(self):
        assert hasattr(UsersController, "disable_user")

    def test_has_enable_user(self):
        assert hasattr(UsersController, "enable_user")

    def test_has_reset_user_traffic(self):
        assert hasattr(UsersController, "reset_user_traffic")

    def test_has_create_user(self):
        assert hasattr(UsersController, "create_user")

    def test_has_update_user(self):
        assert hasattr(UsersController, "update_user")

    def test_has_delete_user(self):
        assert hasattr(UsersController, "delete_user")

    def test_has_get_all_users(self):
        assert hasattr(UsersController, "get_all_users")

    def test_has_get_user_by_uuid(self):
        assert hasattr(UsersController, "get_user_by_uuid")

    def test_has_get_user_by_short_uuid(self):
        assert hasattr(UsersController, "get_user_by_short_uuid")

    def test_has_get_user_by_username(self):
        assert hasattr(UsersController, "get_user_by_username")

    def test_has_get_user_by_id(self):
        assert hasattr(UsersController, "get_user_by_id")

    def test_has_get_users_by_telegram_id(self):
        assert hasattr(UsersController, "get_users_by_telegram_id")

    def test_has_get_users_by_email(self):
        assert hasattr(UsersController, "get_users_by_email")

    def test_has_get_users_by_tag(self):
        assert hasattr(UsersController, "get_users_by_tag")

    def test_has_get_all_tags(self):
        assert hasattr(UsersController, "get_all_tags")

    def test_has_get_user_accessible_nodes(self):
        assert hasattr(UsersController, "get_user_accessible_nodes")

    def test_has_get_user_subscription_request_history(self):
        assert hasattr(UsersController, "get_user_subscription_request_history")

    def test_has_get_users_stream(self):
        assert hasattr(UsersController, "get_users_stream")
        assert callable(getattr(UsersController, "get_users_stream"))


class TestSystemControllerEndpoints:
    def test_has_get_recap(self):
        assert hasattr(SystemController, "get_recap")
        assert callable(getattr(SystemController, "get_recap"))

    def test_has_get_metadata(self):
        assert hasattr(SystemController, "get_metadata")

    def test_has_get_stats(self):
        assert hasattr(SystemController, "get_stats")

    def test_has_get_bandwidth_stats(self):
        assert hasattr(SystemController, "get_bandwidth_stats")

    def test_has_get_nodes_statistics(self):
        assert hasattr(SystemController, "get_nodes_statistics")

    def test_has_get_health(self):
        assert hasattr(SystemController, "get_health")

    def test_has_get_nodes_metrics(self):
        assert hasattr(SystemController, "get_nodes_metrics")

    def test_has_get_x25519_key_pair(self):
        assert hasattr(SystemController, "get_x25519_key_pair")

    def test_has_debug_srr_matcher(self):
        assert hasattr(SystemController, "debug_srr_matcher")

    def test_no_encrypt_happ_crypto_link(self):
        # Removed in Remnawave API v2.8.0 (use client-side happ link generation instead)
        assert not hasattr(SystemController, "encrypt_happ_crypto_link")


class TestApiTokensControllerEndpoints:
    def test_has_get_scopes(self):
        assert hasattr(APITokensManagementController, "get_scopes")
        assert callable(getattr(APITokensManagementController, "get_scopes"))


class TestHostsBulkActionsControllerEndpoints:
    def test_has_update_hosts(self):
        assert hasattr(HostsBulkActionsController, "update_hosts")
        assert callable(getattr(HostsBulkActionsController, "update_hosts"))

    def test_no_set_inbound_to_hosts(self):
        # Removed in Remnawave API v2.8.0 (replaced by update_hosts)
        assert not hasattr(HostsBulkActionsController, "set_inbound_to_hosts")

    def test_no_set_port_to_hosts(self):
        # Removed in Remnawave API v2.8.0 (replaced by update_hosts)
        assert not hasattr(HostsBulkActionsController, "set_port_to_hosts")


class TestBandwidthStatsControllerEndpoints:
    def test_has_get_stats_nodes_users_usage(self):
        assert hasattr(BandWidthStatsController, "get_stats_nodes_users_usage")
        assert callable(getattr(BandWidthStatsController, "get_stats_nodes_users_usage"))


class TestIpControlControllerEndpoints:
    def test_has_fetch_user_ips(self):
        assert hasattr(IpControlController, "fetch_user_ips")

    def test_has_get_fetch_ips_result(self):
        assert hasattr(IpControlController, "get_fetch_ips_result")

    def test_has_fetch_users_ips(self):
        assert hasattr(IpControlController, "fetch_users_ips")
        assert callable(getattr(IpControlController, "fetch_users_ips"))

    def test_has_get_fetch_users_ips_result(self):
        assert hasattr(IpControlController, "get_fetch_users_ips_result")
        assert callable(getattr(IpControlController, "get_fetch_users_ips_result"))

    def test_has_drop_connections(self):
        assert hasattr(IpControlController, "drop_connections")
