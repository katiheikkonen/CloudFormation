SecurityGroupIngress:
    IpProtocol: tcp
    FromPort: !Ref ApplicationPort
    ToPort: !Ref ApplicationPort
    CidrIp: 0.0.0.0/0

SecurityGroupIngress:
- !Ref SG2