#!/usr/bin/env python

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See LICENSE for more details.
#
# Copyright (c) 2016 ScyllaDB

import time

from avocado import main

from sdcm.tester import ClusterTester


class CQLExampleTest(ClusterTester):

    """
    Example test of how to establish CQL connections and run commands on them.

    :avocado: enable
    """

    def test_cql_example(self):
        """
        Create a table, run a few sql statements
        """
        node = self.db_cluster.nodes[0]
        session = self.cql_connection_patient(node)
        self.create_ks(session, 'ks', 1)
        session.execute("""
            CREATE TABLE test1 (
                k int,
                c1 int,
                c2 int,
                v1 int,
                v2 int,
                PRIMARY KEY (k, c1, c2)
            );
        """)
        time.sleep(1)
        session.execute("INSERT INTO test1 (k, c1, c2, v1, v2) "
                        "VALUES (1, 2, 3, 4, 5)")
        res = session.execute("SELECT v1, v2 from test1")
        self.log.debug(res)


if __name__ == '__main__':
    main()
